import { PromptInput } from "@/modules/prompt-input";

export default function Home() {
    return (
        <div className="relative flex h-full w-full items-center justify-center">
            <div className="absolute inset-0 hidden">MobileSidebar</div>
            <PromptInput />
        </div>
    );
}
