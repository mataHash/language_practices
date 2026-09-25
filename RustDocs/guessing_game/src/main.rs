use rand::Rng;
use std::cmp::Ordering;
use std::io;
fn main() {
    println!("Guess the Number!");
    loop {
        println!("Please input your guess!");

        let mut guess = String::new();
        let secret_number = rand::thread_rng().gen_range(1..=100);
        println!("the secret number is {secret_number}");
        io::stdin()
            .read_line(&mut guess)
            .expect("failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("you guessed {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("too small"),
            Ordering::Greater => println!("too big"),
            Ordering::Equal => {
                println!("Congrats You win");
                break;
            }
        }
    }
}
