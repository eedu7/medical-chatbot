import React from "react";
import {
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from "@/components/ui/sidebar";
import { Poppins } from "next/font/google";
import { cn } from "@/lib/utils";
import { CheckIcon, ChevronUp, Loader2, MessageCircleDashedIcon, PlusCircleIcon, User2Icon } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { ScrollArea } from "@/components/ui/scroll-area";
import { prompts } from "@/modules/sidebar/constants";
import Link from "next/link";

const poppins = Poppins({
    subsets: ["latin"],
    weight: ["700"],
});

export const HomeSidebar = () => {
    return (
        <Sidebar collapsible="icon">
            <SidebarHeader>
                <Button
                    size="icon"
                    variant="ghost"
                    className={cn(poppins.className, "w-full")}
                >
                    <Loader2 />
                    AI Medical Chatbot
                </Button>
            </SidebarHeader>
            <SidebarContent className="overflow-hidden">
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
                <SidebarGroup className="h-full">
                    <SidebarGroupLabel>Recents</SidebarGroupLabel>
                    <SidebarMenu className="text-muted-foreground h-full font-medium">
                        <ScrollArea className="h-full">
                            {prompts.map((value, index) => (
                                <SidebarMenuItem key={index}>
                                    <SidebarMenuButton className="cursor-pointer text-xs hover:text-black">
                                        <p className="line-clamp-1">{value}</p>
                                    </SidebarMenuButton>
                                </SidebarMenuItem>
                            ))}
                        </ScrollArea>
                    </SidebarMenu>
                </SidebarGroup>
            </SidebarContent>
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
                                                    <p className="text-muted-foreground text-xs font-medium">
                                                        Free plan
                                                    </p>
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
        </Sidebar>
    );
};
