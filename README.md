# noman - Man pages without the man

**noman** is a command-line tool and website that provides AI-generated, human-friendly “man pages.” Unlike traditional man pages—often seen as too verbose or cryptic—**noman** uses AI to summarize and clarify command usage, making it easier to understand. No man behind these man pages.


## Features

- **AI-Generated Help**
  `noman` uses AI to generate concise explanations and examples for various Unix commands. Given the AI's strong training in programming-related topics, it provides reliable descriptions for established UNIX commands.
- **Simplified Language**
  We minimize jargon and explain things in everyday terms, so you don’t have to dig through long or confusing docs.
- **Focused, Not Exhaustive**
  noman doesn't aim to document every obscure feature of a command. Instead, it highlights the most common and practical use cases, avoiding overly technical or academic details that aren't useful in day-to-day work.
- **Practical Examples**
  Each command’s page focuses on real-world use cases and common options.
- **Freqentry Asked Questions(FAQ)**
  `noman` includes a section for frequently asked questions, addressing common pitfalls and best practices.
- **Pre-Generated Pages**
  `noman` includes pre-generated pages, allowing for immediate display of help information at no cost. Currently, **noman** covers over 100 core commands, with emphasis on those found in GNU coreutils.

## What makes noman a good idea?

`noman` is a highly practical project that addresses a common pain point: traditional Unix man pages are often difficult for beginners or non-experts to understand. Using AI to simplify these explanations is an effective and innovative solution.

## No more waiting or typing long questions

Traditional man pages might be verbose, but at least they're quick—you just type `man ls` and the information appears instantly. In contrast, asking AI usually involves opening a browser, navigating to a website, typing a question like “How do I use the ls command?” and waiting several seconds for a response. `noman` solves this by pre-generating documentation, giving you immediate access without delay.


## Why AI works well here

It is widely recognized that AI-generated technical explanations often fall short in terms of clarity and accuracy. However, in the case of Unix commands—a well-established and thoroughly documented domain—AI systems have a distinct advantage: they can reference authoritative sources to produce reliable content with minimal risk of error. By customizing prompts for each command, we enhance both the precision and clarity of the output. Furthermore, all generated content undergoes human review to ensure correctness and practical relevance.

## Why noman is safer than searching on your own

While users can always search online or ask general-purpose AI tools for help, those methods often produce inconsistent or inaccurate results depending on how the question is phrased. By contrast, noman uses carefully designed prompts and consistent formatting to reduce ambiguity and increase reliability. Although no AI-generated content is entirely error-free, noman offers a safer and more user-friendly alternative to ad-hoc searching, especially for beginners.

## Low maintenance cost

`noman` requires virtually no human intervention. Since pages are AI-generated, there's no need for manual updates or editorial work—the only cost is the AI API fee! This approach makes it incredibly easy to expand documentation by simply adding new commands or refining prompts, resulting in immediate quality improvements without the traditional overhead of documentation maintenance.

## Community-driven quality improvement

While noman uses AI to generate documentation, we still value human feedback! Report any inaccuracies or areas for improvement through GitHub issues, and we'll use that feedback to refine our prompts and regenerate pages. This collaborative approach combines the efficiency of AI generation with the expertise of our community, creating a continuous improvement cycle that keeps documentation accurate and helpful without requiring extensive manual editing.

## Installation

1. **Prerequisites**  
   - Python 3.10+ (recommended)  

2. **Install via pip (example)**  
   ```bash
   pip install noman
   ```

3. **Clone from GitHub (if applicable)**  
   ```bash
   git clone https://github.com/yourusername/noman.git
   cd noman
   pip install -r requirements.txt
   ```



## Contributing

We welcome all contributions! Feel free to:

- **Open Issues**: Found a bug or have a feature request? Let us know.  
- **Submit Pull Requests**: Improve existing code or add new features.  
- **Enhance Documentation**: If you find something unclear, help make it clearer for everyone.

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/noman.git
   cd noman
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```
3. Rebuild pages
   ```bash
   uv run pyprod pages/ja/ls.md
   ```

## License

I'm not sure if AI-generated content itself can be copyrighted. Anyway, this project is licensed under the [MIT License](LICENSE) License—you’re free to use, modify, and distribute it under the terms of the license.

## Disclaimer

- AI-generated content can sometimes contain inaccuracies. Always verify critical commands or options, especially in production environments.  
