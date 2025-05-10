import React from "react";

import { SidebarProvider } from "@/components/ui/sidebar";
import { HomeSidebar } from "@/modules/sidebar";

export default function HomeLayout({ children }: { children: React.ReactNode }) {
    return (
        <div className="min-h-screen">
            <SidebarProvider>
                <HomeSidebar />
                <div className="relative">
                    <main className="w-full border">{children}</main>
                </div>
            </SidebarProvider>
        </div>
    );
}
