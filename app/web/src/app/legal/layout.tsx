import React from "react";

export default function LegalLayout({ children }: { children: React.ReactNode }) {
    return (
        <div className="flex min-h-screen flex-col">
            <main className="h-full flex-1">{children}</main>
        </div>
    );
}
