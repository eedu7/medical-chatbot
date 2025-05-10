import React from "react";
import { Sidebar, SidebarContent } from "@/components/ui/sidebar";
import { Footer } from "@/modules/sidebar/Footer";
import { ActionGroup } from "@/modules/sidebar/ActionGroup";
import { PreviousChatGroup } from "@/modules/sidebar/PreviousChatGroup";
import { Header } from "@/modules/sidebar/Header";

export const HomeSidebar = () => {
    return (
        <Sidebar collapsible="icon">
            <Header />
            <SidebarContent className="overflow-hidden">
                <ActionGroup />
                <PreviousChatGroup />
            </SidebarContent>
            <Footer />
        </Sidebar>
    );
};
