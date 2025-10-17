# Bank-Management-Project-

A simple command-line banking application built with Python that allows users to manage bank accounts with basic operations like account creation, deposits, withdrawals, and account management.

![](https://github.com/Rajni0327/Bank-Management-Project-/blob/main/image.png)

## Features

- **Create Account**: Register a new bank account with personal details
- **Deposit Money**: Add funds to your account (max ₹10,000 per transaction)
- **Withdraw Money**: Withdraw funds from your account
- **View Details**: Display all account information
- **Update Details**: Modify account information (name, email, PIN)
- **Delete Account**: Permanently remove an account

### Menu Options

When you run the program, you'll see the following menu:

```
press 1 for creating an account
press 2 for depositing the money
press 3 for withdrawing the money
press 4 for details
press 5 for updating the details
press 6 for deleting account
```

### Creating an Account

1. Select option `1`
2. Provide the following information:
   - Name
   - Age (must be 18 or older)
   - Email address
   - 4-digit PIN
3. A unique account number will be automatically generated
4. **Important**: Save your account number for future transactions

### Account Number Format

Account numbers are randomly generated using:
- 3 letters (uppercase or lowercase)
- 3 digits
- 1 special character (!@#$%^&*)

Example: `aB3c5!7`

### Depositing Money

1. Select option `2`
2. Enter your account number
3. Enter your 4-digit PIN
4. Specify the amount (must be between ₹1 and ₹10,000)

### Withdrawing Money

1. Select option `3`
2. Enter your account number
3. Enter your 4-digit PIN
4. Specify the amount (must not exceed your balance)

### Viewing Account Details

1. Select option `4`
2. Enter your account number
3. Enter your 4-digit PIN
4. All account information will be displayed

### Updating Account Details

1. Select option `5`
2. Enter your account number
3. Enter your 4-digit PIN
4. Update desired fields (name, email, or PIN)
5. Press Enter to skip fields you don't want to change
6. **Note**: Age, account number, and balance cannot be modified

### Deleting an Account

1. Select option `6`
2. Enter your account number
3. Enter your 4-digit PIN
4. Confirm deletion by pressing `y`

## Data Storage

Account data is stored in `data.json` in the following format:

```json
[
  {
    "name": "John Doe",
    "age": 25,
    "email": "john@example.com",
    "pin": 1234,
    "accountNo": "aB3c5!7",
    "balance": 5000
  }
]
```

## Limitations

- Maximum deposit per transaction: ₹10,000
- Minimum age requirement: 18 years
- PIN must be exactly 4 digits
- Single-user operation (no concurrent transactions)

## Error Handling

The application includes basic error handling for:
- Invalid age or PIN during account creation
- Insufficient funds during withdrawal
- Invalid account credentials
- Missing data file


