import React from "react";
import { SidebarFooter, SidebarMenu, SidebarMenuButton, SidebarMenuItem } from "@/components/ui/sidebar";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { CheckIcon, ChevronUp, User2Icon } from "lucide-react";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";

export const Footer = () => {
    return (
        <SidebarFooter>
            <SidebarMenu>
                <SidebarMenuItem>
                    <DropdownMenu>
                        <DropdownMenuTrigger asChild>
                            <SidebarMenuButton>
                                <User2Icon /> Username
                                <ChevronUp className="ml-auto" />
                            </SidebarMenuButton>
                        </DropdownMenuTrigger>
                        <DropdownMenuContent
                            side="top"
                            className="w-[240px]"
                        >
                            <DropdownMenuGroup>
                                <DropdownMenuItem className="flex flex-col gap-4">
                                    <div className="w-full">
                                        <p className="text-muted-foreground line-clamp-1 font-medium tracking-wide">
                                            username@gmail.com
                                        </p>
                                    </div>
                                    <div className="flex w-full gap-2">
                                        <Avatar>
                                            <AvatarImage
                                                src="https://github.com/shadcn.png"
                                                alt="@shadcn"
                                            />
                                            <AvatarFallback>CN</AvatarFallback>
                                        </Avatar>
                                        <div className="flex w-full items-center justify-between">
                                            <div className="">
                                                <p className="font-medium">Personal</p>
                                                <p className="text-muted-foreground text-xs font-medium">Free plan</p>
                                            </div>
                                            <CheckIcon className="stroke-blue-600" />
                                        </div>
                                    </div>
                                </DropdownMenuItem>
                            </DropdownMenuGroup>
                            <DropdownMenuSeparator />
                            <DropdownMenuGroup>
                                <DropdownMenuItem>Settings</DropdownMenuItem>
                                <DropdownMenuItem>Languages</DropdownMenuItem>
                                <DropdownMenuItem>Get help</DropdownMenuItem>
                            </DropdownMenuGroup>
                            <DropdownMenuSeparator />
                            <DropdownMenuGroup>
                                <DropdownMenuItem>View plans</DropdownMenuItem>
                                <DropdownMenuItem>Learn more</DropdownMenuItem>
                            </DropdownMenuGroup>
                            <DropdownMenuSeparator />
                            <DropdownMenuGroup>
                                <DropdownMenuItem>Log out</DropdownMenuItem>
                            </DropdownMenuGroup>
                        </DropdownMenuContent>
                    </DropdownMenu>
                </SidebarMenuItem>
            </SidebarMenu>
        </SidebarFooter>
    );
};
