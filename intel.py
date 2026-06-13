import anthropic
import sys

def generate_briefing(company_name):
    client = anthropic.Anthropic()
    
    prompt = f"""Generate a structured competitive intelligence briefing for {company_name}.

Include the following sections:

1. COMPANY OVERVIEW
Brief description, size, industry, and business model.

2. RECENT NEWS & DEVELOPMENTS
Key news from the past 6-12 months.

3. FINANCIAL HIGHLIGHTS
Revenue, growth trajectory, and key financial metrics if publicly available.

4. STRATEGIC PRIORITIES
Current strategy, key initiatives, and stated goals.

5. KEY RISKS & HEADWINDS
Main challenges the company is facing.

6. OPPORTUNITIES
Where the company is investing or expanding.

7. LEADERSHIP
Key executives and any recent leadership changes.

Be specific and factual. If information is not available, say so rather than speculating."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text

def main():
    if len(sys.argv) < 2:
        company = input("Enter company name: ")
    else:
        company = " ".join(sys.argv[1:])
    
    print(f"\nGenerating briefing for {company}...\n")
    print("=" * 60)
    
    briefing = generate_briefing(company)
    print(briefing)
    print("=" * 60)

if __name__ == "__main__":
    main()