from dependencies.models.assets import Transaction

async def process_transaction(transaction: Transaction):
    """Format transaction fileds and perform validations before saving to the database"""
    transaction.currency = transaction.currency.lower()
    transaction_cost = transaction.price * transaction.quantity
    if not transaction.total_cost:
        transaction.total_cost = transaction_cost + transaction.costs
    
    return transaction
        