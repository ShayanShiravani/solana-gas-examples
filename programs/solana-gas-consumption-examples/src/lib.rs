use anchor_lang::prelude::*;

declare_id!("DBYZWu2VUr2LypbdN3dh6GKKGxRCi2cyEXGRjPByMTZf");

pub fn my_is_prime(number: u128) -> bool {
    if number <= 1 {
        return false;
    }
    if number <= 3 {
        return true;
    }
    if number % 2 == 0 || number % 3 == 0 {
        return false;
    }
    let mut i: u128 = 5;
    while i * i <= number {
        if number % i == 0 || number % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }
    return true;
}

fn my_fibonacci(n: u128) -> u128 {
    if n <= 1 {
        return n;
    }
    return my_fibonacci(n - 1) + my_fibonacci(n - 2);
}

#[program]
pub mod solana_gas_consumption_examples {
    use super::*;

    pub fn initialize(_ctx: Context<Initialize>) -> Result<()> {
        Ok(())
    }

    pub fn bitwise_operation(_ctx: Context<Operation>, input: u128) -> Result<u128> {
        let mut result: u128 = input << 3;
        result |= 0xF0;
        result &= 0x0F;
        msg!("Result of bitwiseOperation: {}", result);
        Ok(result)
    }

    pub fn sum_of_natural_numbers(_ctx: Context<Operation>, end: u128) -> Result<u128> {
        let mut sum: u128 = 0;
        let mut i: u128 = 0;
        while i <= end {
            sum += i;
            i += 1;
        }
        msg!("Result of sumOfNaturalNumbers: {}", sum);
        Ok(sum)
    }


    pub fn is_prime(_ctx: Context<Operation>, number: u128) -> Result<bool> {
        let result: bool = my_is_prime(number);
        msg!("Result of isPrime: {}", result);
        Ok(result)
    }

    pub fn nth_prime(_ctx: Context<Operation>, n: u128) -> Result<u128> {
        require!(n > 0, MyError::NotPositiveInt);

        let mut number: u128 = 2;
        let mut primes_found: u128 = 0;

        while primes_found < n {
            if my_is_prime(number) {
                primes_found += 1;
            }

            number += 1;
        }
        msg!("Result of nthPrime: {}", number - 1);
        Ok(number - 1)
    }

    pub fn fibonacci(_ctx: Context<Operation>, n: u128) -> Result<u128> {
        let result: u128 = my_fibonacci(n);
        msg!("Result of fibonacci: {}", result);
        Ok(result)
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(mut)]
    pub payer: Signer<'info>,
}

#[derive(Accounts)]
pub struct Operation<> {}

#[error_code]
pub enum MyError {
    #[msg("Input must be a positive integer")]
    NotPositiveInt
}
