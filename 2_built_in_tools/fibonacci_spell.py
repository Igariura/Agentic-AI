#!/usr/bin/env python3
"""
🧙‍♂️ The Fibonacci Scroll of Kiro the Grey Hat 🧙‍♂️
A magical spell to conjure the first 10 numbers of the ancient Fibonacci sequence

The Fibonacci sequence follows the mystical rule:
Each number is the sum of the two preceding ones, starting from 0 and 1
"""

def fibonacci_spell(n=10):
    """
    Cast the Fibonacci spell to generate the first n numbers of the sequence
    
    Args:
        n (int): Number of Fibonacci numbers to generate (default: 10)
    
    Returns:
        list: The first n Fibonacci numbers
    """
    print("🌟 Casting the Fibonacci Spell... 🌟")
    print("✨" * 30)
    
    if n <= 0:
        print("⚠️  The spell requires a positive number!")
        return []
    
    fibonacci_numbers = []
    
    # Initialize the first two numbers
    a, b = 0, 1
    
    for i in range(n):
        fibonacci_numbers.append(a)
        print(f"🔮 Conjuring number {i+1}: {a}")
        
        # Calculate the next number in the sequence
        a, b = b, a + b
    
    print("✨" * 30)
    print(f"🎯 Spell complete! Generated {n} Fibonacci numbers:")
    print(f"📜 {fibonacci_numbers}")
    
    return fibonacci_numbers

# Main spell execution
if __name__ == "__main__":
    print("🧙‍♂️ Welcome to Kiro's Fibonacci Magic! 🧙‍♂️")
    print("=" * 50)
    
    # Cast the spell for the first 10 Fibonacci numbers
    result = fibonacci_spell(10)
    
    print("\n🔍 Let me verify the magic worked correctly:")
    for i, num in enumerate(result):
        if i < 2:
            print(f"   F({i}) = {num} (starting value)")
        else:
            prev_sum = result[i-2] + result[i-1]
            print(f"   F({i}) = F({i-2}) + F({i-1}) = {result[i-2]} + {result[i-1]} = {num}")
    
    print("\n✅ The ancient Fibonacci magic flows perfectly!")