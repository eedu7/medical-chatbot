"use client";

import React from "react";
import {
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarTrigger,
    useSidebar,
} from "@/components/ui/sidebar";
import { cn } from "@/lib/utils";
import { Poppins } from "next/font/google";

const poppins = Poppins({
    subsets: ["latin"],
    weight: ["700"],
});

export const Header = () => {
    const { state } = useSidebar();
    return (
        <SidebarHeader>
            <SidebarMenu>
                <SidebarMenuItem>
                    <div className={cn(state === "expanded" && "flex items-center")}>
                        <SidebarMenuButton
                            asChild
                            className="max-w-fit"
                        >
                            <SidebarTrigger />
                        </SidebarMenuButton>
                        <h1 className={cn(poppins.className, "text-lg tracking-widest")}>Medoc</h1>
                    </div>
                </SidebarMenuItem>
            </SidebarMenu>
        </SidebarHeader>
    );
};
