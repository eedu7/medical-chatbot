import React from "react";

import { SidebarProvider } from "@/components/ui/sidebar";
import { HomeSidebar } from "@/modules/sidebar";

export default function HomeLayout({ children }: { children: React.ReactNode }) {
    return (
        <SidebarProvider>
            <HomeSidebar />
            <div className="flex min-h-screen w-full max-w-screen flex-col">
                <main className="flex-1">{children}</main>
            </div>
        </SidebarProvider>
    );
}
