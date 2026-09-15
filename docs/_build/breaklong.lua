-- PDF-only: shorten known home-directory prefixes, then wrap remaining long
-- paths/URLs so they break at /, _, -, . — never mid-word.
-- Also stop Helvetica Neue AAT ligatures (ff/fi/fl) so names like
-- fcffsimpleginzu stay letter-for-letter.
-- Path wrapping only touches paragraph/plain text, never headings, so the TOC
-- stays clean. Ligature breaking is applied more widely (including headings).

if not FORMAT:match('latex') then
  return {}
end

local ZWNJ = '\u{200C}'

local function shorten(s)
  s = s:gsub('/Users/siddharth/Downloads/financeMD/', 'financeMD/')
  s = s:gsub('/Users/siddharth/Valuation/', 'Valuation/')
  s = s:gsub('/Users/siddharth/%.claude/plans/', 'plans/')
  s = s:gsub('/Users/siddharth/%.claude/projects/[^/]+/[^/]+/', 'claude/')
  s = s:gsub('/Users/siddharth/%.claude/projects/[^/]+/', 'claude/')
  s = s:gsub('/Users/siddharth/%.claude/projects/', 'claude/')
  s = s:gsub('/Users/siddharth/', '~/')
  return s
end

local function latex_url_arg(s)
  s = s:gsub('\\', '\\\\')
  s = s:gsub('%%', '\\%%')
  s = s:gsub('#', '\\#')
  s = s:gsub('{', '\\{')
  s = s:gsub('}', '\\}')
  return s
end

local function pathish(s)
  return s:find('[/_~]') ~= nil
end

-- Peel trailing sentence punctuation so "file.md;" wraps as path + ";".
local function split_trail(s)
  local core, trail = s:match('^(.-)([%.,;:%)%]]+)$')
  if core and core ~= '' then
    return core, trail
  end
  return s, ''
end

-- Insert a break after the first letter of each ff/fi/fl pair.
local function break_pairs(text, insert)
  local out = {}
  local pos = 1
  local n = #text
  local changed = false
  while pos <= n do
    local earliest
    for _, pair in ipairs({ 'ff', 'fi', 'fl' }) do
      local i = text:find(pair, pos, true)
      if i and (not earliest or i < earliest) then
        earliest = i
      end
    end
    if not earliest then
      out[#out + 1] = text:sub(pos)
      break
    end
    out[#out + 1] = text:sub(pos, earliest)
    out[#out + 1] = insert
    changed = true
    pos = earliest + 1
  end
  if not changed then
    return text, false
  end
  return table.concat(out), true
end

local function zwnj_break(text)
  local s = break_pairs(text, ZWNJ)
  return s
end

local function wrap_path(s, code)
  local arg = latex_url_arg(s)
  if code then
    return pandoc.RawInline('latex', '{\\urlstyle{tt}\\nolinkurl{' .. arg .. '}}')
  end
  return pandoc.RawInline('latex', '\\nolinkurl{' .. arg .. '}')
end

-- Code spans that contain spaces (commands, "value_company AAPL US") must keep
-- their spaces, which \nolinkurl drops. Typeset them as plain \texttt with a
-- break opportunity after path punctuation instead.
local function latex_text_escape(s)
  s = s:gsub('\\', '\1')
  s = s:gsub('([{}#%%&%$_])', '\\%1')
  s = s:gsub('~', '\\textasciitilde{}')
  s = s:gsub('%^', '\\textasciicircum{}')
  s = s:gsub('\1', '\\textbackslash{}')
  return s
end

local function wrap_code_tt(s)
  local esc = latex_text_escape(s)
  esc = esc:gsub('([/%-%.])', '%1\\allowbreak{}')
  esc = esc:gsub('(\\_)', '%1\\allowbreak{}')
  return pandoc.RawInline('latex', '\\texttt{' .. esc .. '}')
end

local function emit_path(s, code, trail)
  local out = wrap_path(s, code)
  if trail ~= '' then
    return { out, pandoc.Str(trail) }
  end
  return out
end

-- Helvetica Neue on macOS forms AAT ligatures that fontspec cannot disable.
-- A kern interrupts the glyph run; an empty group does not.
local function deligate_inlines(text)
  local out = {}
  local pos = 1
  local n = #text
  local changed = false
  while pos <= n do
    local earliest
    for _, pair in ipairs({ 'ff', 'fi', 'fl' }) do
      local i = text:find(pair, pos, true)
      if i and (not earliest or i < earliest) then
        earliest = i
      end
    end
    if not earliest then
      out[#out + 1] = pandoc.Str(text:sub(pos))
      break
    end
    if earliest > pos then
      out[#out + 1] = pandoc.Str(text:sub(pos, earliest - 1))
    end
    out[#out + 1] = pandoc.Str(text:sub(earliest, earliest))
    out[#out + 1] = pandoc.RawInline('latex', '\\kern0pt{}')
    changed = true
    pos = earliest + 1
  end
  if not changed then
    return nil
  end
  return out
end

local function fix_body(el)
  local raw = shorten(el.text)
  local s, trail = split_trail(raw)
  local long = #s > 20
  if el.t == 'Str' then
    if pathish(s) and (long or raw ~= el.text) then
      return emit_path(s, false, trail)
    end
    local broken = deligate_inlines(raw)
    if broken then
      return broken
    end
    if raw ~= el.text then
      el.text = raw
      return el
    end
  elseif el.t == 'Code' then
    if raw:find(' ', 1, true) then
      if long or pathish(raw) then
        return wrap_code_tt(raw)
      end
    elseif long or (raw ~= el.text and pathish(raw)) then
      return wrap_path(raw, true)
    end
    local z = zwnj_break(raw)
    if z ~= el.text then
      el.text = z
      return el
    end
  end
end

local function walk_body(b)
  return b:walk({ Str = fix_body, Code = fix_body })
end

local function fix_header_str(el)
  local z = zwnj_break(el.text)
  if z ~= el.text then
    el.text = z
    return el
  end
end

local function Header(el)
  return el:walk({ Str = fix_header_str, Code = fix_header_str })
end

local function CodeBlock(el)
  el.text = zwnj_break(shorten(el.text))
  return el
end

return {
  { Para = walk_body, Plain = walk_body, Header = Header, CodeBlock = CodeBlock },
}
