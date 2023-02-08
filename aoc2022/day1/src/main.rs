fn main() {
    //reading input , handling error using defualt by unwrap.
    //let mut input = std::fs::read_to_string("src/input.txt").unwrap();
    let input = std::fs::read_to_string("src/input.txt");
    match input {
        Ok(s) => s,
        Err(e) => panic!("Couldnt read src/input.txt ,{e}"),
    };
}
