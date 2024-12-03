let file = "input.txt"

let () =
  print_endline "advent of code day 1!";
  let ic = open_in file in
  try close_in ic
  with e ->
    close_in_noerr ic;
    raise e
