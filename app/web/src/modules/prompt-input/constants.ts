import {
    ActivityIcon,
    BookOpenIcon,
    BrainIcon,
    FileTextIcon,
    HelpCircleIcon,
    LayoutDashboardIcon,
    LucideIcon,
    RefreshCcwIcon,
    StethoscopeIcon,
    UploadIcon,
    UserPlusIcon,
} from "lucide-react";

interface SpecificPrompts {
    name: string;
    icon: LucideIcon;
}

export const specificPrompts: SpecificPrompts[][] = [
    [
        {
            name: "Diagnose",
            icon: StethoscopeIcon,
        },
        {
            name: "Explain",
            icon: BrainIcon,
        },
        {
            name: "Learn more",
            icon: BookOpenIcon,
        },
        {
            name: "Ask a doctor",
            icon: UserPlusIcon,
        },
    ],
    [
        {
            name: "Risk factors",
            icon: ActivityIcon,
        },
        {
            name: "Medical report",
            icon: FileTextIcon,
        },
        {
            name: "Compare cases",
            icon: LayoutDashboardIcon,
        },
        {
            name: "Upload scan",
            icon: UploadIcon,
        },
        {
            name: "Second opinion",
            icon: RefreshCcwIcon,
        },
        {
            name: "Ask why",
            icon: HelpCircleIcon,
        },
    ],
];
