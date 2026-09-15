-- Reading annotations are explicit Markdown, not inferred from keywords.
-- Standard builds remove guidance and unwrap emphasis, preserving source prose.
local reading = false
local map_path = nil
local book = '01'
local root = '.'
local kinds = {
  ['read-first'] = {'ReadingBlue', 'READ FIRST'},
  ['key-idea'] = {'ReadingTeal', 'KEY IDEA'},
  ['watch-out'] = {'ReadingOrange', 'WATCH OUT'},
  ['optional'] = {'ReadingPurple', 'OPTIONAL - FIRST PASS'},
}
local function has(el, name) return el.classes:includes(name) end
local function meta(m)
  reading = m['reading-edition'] == true or pandoc.utils.stringify(m['reading-edition'] or '') == 'true'
  if m['reading-map'] then map_path = pandoc.utils.stringify(m['reading-map']) end
  if m['reading-book'] then book = pandoc.utils.stringify(m['reading-book']) end
  if m['reading-root'] then root = pandoc.utils.stringify(m['reading-root']) end
end
local function picture(el)
  if reading and FORMAT:match('latex') and not el.src:match('^/') and not el.src:match('^%a+://') then
    local diagram=el.src:match('^diagrams/png/([^/]+)%.png$')
    if diagram then
      el.src=root .. '/../tmp/pdfs/diagrams/' .. diagram .. '.pdf'
      if diagram=='milestone-map' then el.attributes.height='7.2in'
      else el.attributes.width='100%' end
    else el.src = root .. '/' .. el.src end
    return el
  end
end
local function div(el)
  if not reading then
    if has(el, 'reading-only') then return {} end
    if has(el, 'reading-emphasis') then return el.content end
    return nil
  end
  for name, style in pairs(kinds) do
    if has(el, name) and (has(el, 'reading-only') or has(el, 'reading-emphasis')) then
      if FORMAT:match('latex') then
        local result = pandoc.List({pandoc.RawBlock('latex', '\\begin{readingbox}{' .. style[1] .. '}{' .. style[2] .. '}')})
        result:extend(el.content)
        result:insert(pandoc.RawBlock('latex', '\\end{readingbox}'))
        return result
      end
    end
  end
end
local function span(el)
  local colors={['legend-blue']='ReadingBlue',['legend-teal']='ReadingTeal',['legend-orange']='ReadingOrange',['legend-purple']='ReadingPurple'}
  if reading and FORMAT:match('latex') then
    for class,color in pairs(colors) do
      if has(el,class) then
        local result=pandoc.List({pandoc.RawInline('latex','\\textcolor{'..color..'}{')})
        result:extend(el.content);result:insert(pandoc.RawInline('latex','}'));return result
      end
    end
  end
  if has(el, 'reading-highlight') then
    if reading and FORMAT:match('latex') then
      local result = pandoc.List({pandoc.RawInline('latex', '\\ReadingHighlight{')})
      result:extend(el.content)
      result:insert(pandoc.RawInline('latex', '}'))
      return result
    end
    return el.content
  end
end
local function code(el)
  if not reading or not FORMAT:match('latex') then return end
  if #el.text>20 then return end -- retain the existing long-path shortening pass
  -- Preserve short identifiers too: narrow cells need breaks at punctuation.
  local s=el.text
  s=s:gsub('\\','\1'):gsub('([{}#%%&%$_])','\\%1')
  s=s:gsub('~','\\textasciitilde{}'):gsub('%^','\\textasciicircum{}'):gsub('\1','\\textbackslash{}')
  s=s:gsub('([/%-%.])','%1\\allowbreak{}'):gsub('(\\_)','%1\\allowbreak{}')
  s=s:gsub('f([fil])','f\\kern0pt{}%1')
  return pandoc.RawInline('latex','\\texttt{'..s..'}')
end
local function table_style(el)
  if not reading or not FORMAT:match('latex') then return end
  -- Pandoc's table head may contain more than one row. Shade each explicitly.
  for _, row in ipairs(el.head.rows) do
    if row.cells[1] and row.cells[1].contents[1] then
      local block = row.cells[1].contents[1]
      if block.t == 'Plain' or block.t == 'Para' then
        block.content:insert(1, pandoc.RawInline('latex', '\\cellcolor{ReadingTable}'))
      end
    end
    for i=2,#row.cells do
      local block = row.cells[i].contents[1]
      if block and (block.t == 'Plain' or block.t == 'Para') then
        block.content:insert(1, pandoc.RawInline('latex', '\\cellcolor{ReadingTable}'))
      end
    end
  end
  local n=#el.colspecs
  -- Text-heavy tables keep room for prose; numbering columns stay compact.
  local totals={}
  for i=1,n do totals[i]=20 end
  for _,body in ipairs(el.bodies) do
    for _,row in ipairs(body.body) do
      for i,cell in ipairs(row.cells) do totals[i]=totals[i]+#pandoc.utils.stringify(cell.contents) end
    end
  end
  local content_size=0
  for i=1,n do content_size=content_size+totals[i] end
  local sum=0
  for i=1,n do totals[i]=math.sqrt(totals[i]);sum=sum+totals[i] end
  for i=1,n do el.colspecs[i][2]=0.04+(1-0.04*n)*totals[i]/sum end
  local headings={}
  if el.head.rows[1] then
    for i,cell in ipairs(el.head.rows[1].cells) do headings[i]=pandoc.utils.stringify(cell.contents) end
  end
  if n==4 and headings[1]=='Class' then
    local widths={0.24,0.27,0.24,0.25}
    for i=1,n do el.colspecs[i][2]=widths[i] end
  elseif n==7 and headings[1]=='Week' then
    local widths={0.06,0.09,0.13,0.14,0.22,0.20,0.16}
    for i=1,n do el.colspecs[i][2]=widths[i] end
  end
  local begin='{\\small\\setlength{\\tabcolsep}{4pt}\n'
  local finish='\n}'
  if n>=6 or (n==5 and content_size>2500) then begin='\\begin{landscape}\n'..begin;finish=finish..'\n\\end{landscape}' end
  return {pandoc.RawBlock('latex',begin),el,pandoc.RawBlock('latex',finish)}
end
local function heading(el)
  if not reading or not FORMAT:match('latex') then return end
  local s=pandoc.utils.stringify(el)
  if el.level==1 then return {pandoc.RawBlock('latex','\\Needspace{140pt}'),el} end
  if s=='Three things to remember' or s=='Done when' then
    return {pandoc.RawBlock('latex','\\Needspace{160pt}'),el}
  end
end
local function para(el)
  if not reading or not FORMAT:match('latex') then return end
  local s = pandoc.utils.stringify(el)
  if s:match('^Source:') or s:match('^Sources:') then
    return {pandoc.RawBlock('latex', '{\\small\\color{ReadingSource}\\raggedright'),el,pandoc.RawBlock('latex','\\par}')}
  end
end
local function quote(el)
  if reading and FORMAT:match('latex') and pandoc.utils.stringify(el):match('^Comment') then
    local body=pandoc.Div(el.content):walk({SoftBreak=function() return pandoc.LineBreak() end})
    return {pandoc.RawBlock('latex','\\begin{readingcomment}'),body,pandoc.RawBlock('latex','\\end{readingcomment}')}
  end
end
local function document(doc)
  if not reading or not FORMAT:match('latex') then return end
  -- Keep a heading with its short orientation or takeaway panel. A section
  -- heading otherwise allows a page break before a breakable tcolorbox.
  local grouped=pandoc.List({})
  local i=1
  while i<=#doc.blocks do
    local b=doc.blocks[i]
    local next_block=doc.blocks[i+1]
    if b.t=='Header' and next_block and next_block.t=='RawBlock' and next_block.text:match('^\\begin{readingbox}') then
      local finish=i+2
      while finish<=#doc.blocks and not (doc.blocks[finish].t=='RawBlock' and doc.blocks[finish].text=='\\end{readingbox}') do finish=finish+1 end
      assert(finish<=#doc.blocks,'Unclosed reading box')
      grouped:insert(pandoc.RawBlock('latex','\\noindent\\begin{minipage}{\\linewidth}'))
      for j=i,finish do grouped:insert(doc.blocks[j]) end
      grouped:insert(pandoc.RawBlock('latex','\\end{minipage}\\par\\medskip'))
      i=finish+1
    else grouped:insert(b);i=i+1 end
  end
  doc.blocks=grouped
  assert(map_path, 'Reading build requires reading-map metadata')
  local f = assert(io.open(map_path, 'r'))
  local map = pandoc.read(f:read('*a'), 'markdown'); f:close()
  map=map:walk({Span=span,Table=table_style})
  local front = pandoc.List({pandoc.RawBlock('latex','\\def\\ReadingNumber{' .. book .. '}')})
  -- This marker is handled before the title by the metadata header include.
  doc.meta['header-includes'] = doc.meta['header-includes'] or pandoc.MetaList({})
  doc.meta['header-includes']:insert(pandoc.MetaBlocks({pandoc.RawBlock('latex','\\def\\ReadingNumber{' .. book .. '}')}))
  front:extend(map.blocks)
  front:insert(pandoc.RawBlock('latex','\\clearpage\n\\tableofcontents\n\\clearpage'))
  front:extend(doc.blocks)
  doc.blocks = front
  return doc
end
return {{Meta=meta},{Div=div,Span=span,Code=code,Table=table_style,Para=para,BlockQuote=quote,Image=picture,Header=heading},{Pandoc=document}}
