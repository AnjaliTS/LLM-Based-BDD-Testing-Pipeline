#!/usr/bin/env python3
"""
Gherkin Generator for LLM-BDD System
Generates proper Gherkin scenarios
"""
import openai
from config import OPENAI_API_KEY

class GherkinGenerator:
    def __init__(self):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    def generate_gherkin(self, requirements):
        """Generate proper Gherkin scenarios"""
        
        prompt = f"""
        You are a BDD testing expert. Create Gherkin feature files.
        
        Requirements: {requirements}
        
        Create a complete Gherkin feature file with:
        1. Feature description (As a... I want... So that...)
        2. Positive scenarios (tagged with @positive)
        3. Negative scenarios (tagged with @negative)
        4. Proper Gherkin syntax (Given/When/Then)
        5. Concrete examples (use actual values like "standard_user", "secret_sauce")
        
        Format example:
        Feature: User Login
          As a user
          I want to login to the system
          So that I can access my account
          
          @positive @happy
          Scenario: Successful login with valid credentials
            Given I am on the login page
            When I enter "standard_user" as username
            And I enter "secret_sauce" as password
            And I click the login button
            Then I should be redirected to the dashboard
            And I should see "Products" header
            
          @negative
          Scenario: Failed login with invalid password
            Given I am on the login page
            When I enter "standard_user" as username
            And I enter "wrong_password" as password
            And I click the login button
            Then I should see error message "Invalid credentials"
            And I should remain on the login page
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a Gherkin expert. Always output proper Gherkin syntax."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"AI Error: {e}")
            return self._get_sample_gherkin()
    
    def _get_sample_gherkin(self):
        """Return sample Gherkin if AI fails"""
        return """
Feature: E-commerce Shopping
  As a customer
  I want to purchase products online
  So that I can shop conveniently

  @positive @happy
  Scenario: Successful product purchase
    Given I am logged in as "standard_user"
    And I am on the products page
    When I click "Add to Cart" on "Sauce Labs Backpack"
    And I click the shopping cart icon
    And I click "Checkout"
    And I fill in shipping information
    And I click "Continue"
    And I click "Finish"
    Then I should see "Thank you for your order!"
    And I should receive order confirmation

  @negative
  Scenario: Checkout with empty cart
    Given I am logged in as "standard_user"
    And my shopping cart is empty
    When I click the shopping cart icon
    And I try to click "Checkout"
    Then "Checkout" button should be disabled
    And I should see "Your cart is empty" message

  @positive @happy
  Scenario: Search for products
    Given I am logged in as "standard_user"
    When I type "backpack" in the search field
    And I press Enter
    Then I should see "Sauce Labs Backpack" in results
    And I should not see "Sauce Labs Bike Light"
"""
    
    def save_gherkin_file(self, gherkin_content, filename="generated_scenarios.feature"):
        """Save Gherkin to .feature file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(gherkin_content)
        print(f"✅ Gherkin saved to: {filename}")
        return filename

def main():
    """Test the Gherkin generator"""
    print("🧪 Testing Gherkin Generator...")
    
    requirements = input("Enter requirements: ").strip()
    if not requirements:
        requirements = "Users should login and buy products"
    
    generator = GherkinGenerator()
    gherkin = generator.generate_gherkin(requirements)
    
    print("\n" + "=" * 70)
    print("✅ GENERATED GHERKIN SCENARIOS:")
    print("=" * 70)
    print(gherkin)
    print("=" * 70)
    
    # Save to file
    generator.save_gherkin_file(gherkin)
    
    # Count scenarios
    scenarios = gherkin.count("Scenario:")
    positive = gherkin.count("@positive")
    negative = gherkin.count("@negative") - gherkin.count("@positive")
    
    print(f"\n📊 Statistics:")
    print(f"  Total Scenarios: {scenarios}")
    print(f"  Positive (@positive): {positive}")
    print(f"  Negative (@negative): {negative}")

if __name__ == "__main__":
    main()