# Gerbers Cafe Payment System

## Overview
An interactive Python payment system for a cafe that handles:
- Drink selection from 9 different beverages
- Custom add-ons specific to each drink type
- Double shot options for espresso drinks
- Itemized receipts with tax calculation
- Grand total calculation

## Features
- **User Input Validation:** Ensures valid drink selections
- **Context-Aware Add-ons:** Different drinks offer different add-on options
  - Black Coffee: sugar, cream
  - Tea: honey, lemon
  - Cocoa: marshmallows, whipped cream
  - Espresso drinks: dairy-free milk, double shot
- **Pricing Logic:** Correctly calculates base price + add-ons + tax
- **Itemized Receipt:** Shows each drink with all add-ons and individual totals
- **Tax Calculation:** 8.5% tax applied to each order
- **Grand Total:** Returns final amount including all orders and taxes

## How to Run
```bash
python cafe_payment.py
```

Then follow the prompts to:
1. Select a drink (1-9)
2. Choose add-ons specific to that drink
3. Order another drink or checkout
4. View itemized receipt with grand total

## Example Usage
- Customer orders a Latte with dairy-free milk and a double shot
- System calculates: $4.00 (latte) + $0.50 (dairy-free) + $2.00 (double shot) = $6.50
- Tax added: $6.50 × 0.085 = $0.55
- Total with tax: $7.05

## Technical Details
- Uses dictionaries for menu data
- Implements tax calculations and rounding
- Tracks multiple orders in a list
- Formats currency output to 2 decimal places
```

---

## HOW TO ADD IT TO GITHUB

1. **Create the folder structure:**
   - In GitHub Desktop, navigate to your repo
   - Create `/projects/cafe-payment-system/` folder

2. **Add your files:**
   - Copy `cafe_payment.py` into that folder
   - Create `README.md` (use the text above)

3. **Commit:**
```
   Summary: Add Cafe Payment System project
   Description: Interactive Python payment system with user input, 
   add-on selection, itemized receipts, and tax calculation