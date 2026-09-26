import type { Metadata } from "next";
import { Geist, Geist_Mono, Newsreader } from "next/font/google";
import { Nav } from "../components/nav";
import { Providers } from "../components/providers";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const newsreader = Newsreader({
  variable: "--font-newsreader",
  subsets: ["latin"],
  style: ["normal", "italic"],
});

export const metadata: Metadata = {
  title: "Diversify — stories, not tickers",
  description:
    "A long-horizon portfolio tool in the spirit of Damodaran and Buffett: diversify the stories, philosophies, and political regimes you are silently betting on.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} ${newsreader.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col text-ink">
        <Providers>
          <Nav />
          <div className="flex-1">{children}</div>
        </Providers>
      </body>
    </html>
  );
}
