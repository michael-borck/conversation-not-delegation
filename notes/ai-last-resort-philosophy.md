# The "AI Last" Principle: Solve What You Can First

## The Core Idea

Before reaching for an AI tool, solve as much of the problem as you can with conventional means. Use your own expertise, traditional tools, and established workflows first. Only hand off to AI the parts you genuinely cannot solve yourself.

This is not anti-AI. It is pro-efficiency. AI is powerful, but it is also expensive, token-hungry, and often overkill for tasks that a developer can knock out in seconds with the right tools and knowledge.

## Why This Works

**You already know more than you think.** Most tasks in a typical workflow have well-understood solutions. Formatting, linting, simple refactors, boilerplate structure, file organisation -- these do not need a large language model. They need a competent practitioner using the tools already on their machine.

**AI costs compound at scale.** Every token sent and received costs money. In an API context, those costs multiply across users, requests, and iterations. Even in subscription-based tools, you are burning through rate limits and context windows. The less you send to the model, the further your budget stretches.

**Smaller, focused prompts produce better results.** When you have already narrowed the problem down to the specific hard part, the AI has less ambiguity to deal with. You get more precise, useful output because you have done the cognitive work of framing the question well.

**You stay sharp.** Outsourcing every decision to AI erodes your own problem-solving ability over time. Doing the groundwork yourself keeps your skills current and your understanding deep.

## The Practical Workflow

1. **Start with what you know.** Write the code, draft the document, structure the data. Get as far as you can on your own.

2. **Use conventional tools for conventional problems.** Linters, formatters, regex, shell scripts, spreadsheet formulas, templates. These are fast, free, and deterministic.

3. **Identify the genuine sticking point.** What specifically are you stuck on? A tricky algorithm? An unfamiliar API? A complex data transformation you cannot reason through?

4. **Now bring in AI, scoped tightly.** Give it the specific problem, the relevant context, and a clear question. Do not dump your entire project and say "fix this."

5. **Validate and integrate the output yourself.** AI gives you a draft, not a finished product. You still own the result.

## Where AI Earns Its Keep

The principle is not "never use AI." It is "use AI where it adds value you cannot easily generate yourself." That includes things like exploring unfamiliar domains where you lack expertise, generating boilerplate for frameworks you rarely use, debugging complex interactions across multiple systems, brainstorming approaches to novel problems, and processing or transforming data at a scale that would take hours manually.

The key distinction is between using AI as a crutch for laziness versus using it as a lever for capability. The former wastes money and dulls your skills. The latter multiplies your effectiveness.

## The Cost Argument

For developers working with AI APIs, every unnecessary token is wasted spend. But even for those on flat-rate subscriptions, the principle holds. Context windows are finite. Rate limits exist. And the time spent crafting prompts, waiting for responses, and fixing AI-generated mistakes has a real cost in hours and focus.

The most cost-effective AI usage pattern is simple: minimise what you send, maximise the value of what comes back.

## Further Reading

- Efimenko, A. (2026). "7 Ways to Reduce AI Agent Tokens Consumption." *Medium*. https://medium.com/@alexefimenko/7-ways-to-stop-wasting-money-on-ai-tokens-d15a8e235694

- Obed, E. (2025). "Am I Losing My Problem-Solving Skills to AI? A Personal Reflection on Staying Sharp in the AI Era." *Medium*. https://medium.com/@ehoneahobed/am-i-losing-my-problem-solving-skills-to-ai-a-personal-reflection-on-staying-sharp-in-the-ai-era-7166b94ba0c4

- "The Hidden Economics of AI Agents: Managing Token Costs and Latency Trade-offs." (2026). *Stevens Institute of Technology, Stevens Online*. https://online.stevens.edu/blog/hidden-economics-ai-agents-token-costs-latency/

- "How to Reduce LLM Costs: Effective Strategies." (2024). *PromptLayer Blog*. https://blog.promptlayer.com/how-to-reduce-llm-costs/

- "LLM Cost Optimization Guide: Reduce AI Infrastructure 30%." (2025). *FutureAGI*. https://futureagi.com/blogs/llm-cost-optimization-2025
