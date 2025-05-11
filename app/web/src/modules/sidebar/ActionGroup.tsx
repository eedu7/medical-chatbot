import React from "react";
import {
    SidebarGroup,
    SidebarGroupContent,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from "@/components/ui/sidebar";
import Link from "next/link";
import { MessageCircleDashedIcon, PlusCircleIcon } from "lucide-react";
import { Button } from "@/components/ui/button";

export const ActionGroup = () => {
    return (
        <SidebarGroup>
            <SidebarGroupContent>
                <SidebarMenu>
                    <SidebarMenuItem>
                        <SidebarMenuButton asChild>
                            <Link
                                href="#"
                                className="bg-background hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50 flex w-full cursor-pointer items-center justify-start gap-1 border shadow-xs"
                            >
                                <PlusCircleIcon />
                                <span className="font-medium">New chat</span>
                            </Link>
                        </SidebarMenuButton>
                    </SidebarMenuItem>
                    <SidebarMenuItem>
                        <SidebarMenuButton asChild>
                            <Button
                                className="text-muted-foreground flex w-full cursor-pointer items-center justify-start gap-1 hover:text-black"
                                variant="ghost"
                            >
                                <MessageCircleDashedIcon />
                                <span className="font-medium">Chats</span>
                            </Button>
                        </SidebarMenuButton>
                    </SidebarMenuItem>
                </SidebarMenu>
            </SidebarGroupContent>
        </SidebarGroup>
    );
};
