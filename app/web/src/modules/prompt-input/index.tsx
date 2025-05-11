import React from "react";
import { Button } from "@/components/ui/button";
import { specificPrompts } from "@/modules/prompt-input/constants";

export const PromptInput = () => {
    return (
        <section className="flex flex-col gap-4">
            <div>Prompt Input</div>
            <div className="grid grid-cols-3 gap-2 lg:grid-cols-5">
                {specificPrompts[0].map(({ name, icon: Icon }) => (
                    <Button
                        key={name}
                        variant="ghost"
                        size="sm"
                        className="cursor-pointer items-center border"
                    >
                        <Icon />
                        <p>{name}</p>
                    </Button>
                ))}
            </div>
        </section>
    );
};
