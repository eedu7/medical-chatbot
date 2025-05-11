import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import TanstackReactQueryProvider from "@/lib/providers/TanstackReactQueryProvider";

const geistSans = Geist({
    variable: "--font-geist-sans",
    subsets: ["latin"],
});

const geistMono = Geist_Mono({
    variable: "--font-geist-mono",
    subsets: ["latin"],
});

export const metadata: Metadata = {
    title: "AI Medical Chatbot",
    description: "AI-Powered Multi-Cancer Detection and Medical Chatbot",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
            <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
                <TanstackReactQueryProvider>{children}</TanstackReactQueryProvider>
            </body>
        </html>
    );
}
