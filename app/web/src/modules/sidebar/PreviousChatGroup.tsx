"use client";

import React from "react";
import { SidebarGroup, SidebarGroupLabel, SidebarMenu, SidebarMenuItem, useSidebar } from "@/components/ui/sidebar";
import { ScrollArea } from "@/components/ui/scroll-area";
import { prompts } from "@/modules/sidebar/constants";
import Link from "next/link";

export const PreviousChatGroup = () => {
    const { state } = useSidebar();

    if (state === "collapsed") return null;

    return (
        <SidebarGroup className="h-full">
            <SidebarGroupLabel>Recents</SidebarGroupLabel>
            <SidebarMenu className="text-muted-foreground h-full font-medium">
                <ScrollArea className="h-full">
                    <div className="space-y-3">
                        {prompts.map((value, index) => (
                            <SidebarMenuItem key={index}>
                                {/*TODO: Added proper links*/}
                                <Link
                                    href="/"
                                    className="text-muted-foreground cursor-pointer text-sm hover:text-black"
                                >
                                    <p className="line-clamp-1">{value}</p>
                                </Link>
                            </SidebarMenuItem>
                        ))}
                    </div>
                </ScrollArea>
            </SidebarMenu>
        </SidebarGroup>
    );
};
