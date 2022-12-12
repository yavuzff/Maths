type 'a lazylist = 
  |End
  |Rest of 'a *  (unit -> 'a lazylist);;

let rec intstream k = Rest(k,fun () -> intstream (k+1));;

let rec streamfilter f = function 
  |End -> End
  |Rest(x,xf) -> if f x then Rest(x, fun () -> streamfilter f (xf ())) else streamfilter f (xf ());;

let firstn n stream =
  let rec inner acc i s = 
    match i,s with
      |0,_ -> acc
      |_,End -> acc
      |i, Rest(x,xf) -> inner (x::acc) (i-1) (xf()) 
  in
  List.rev (inner [] n stream);;

let getprimes n = 
  let rec sieve = function
    |End -> End
    |Rest(x,xf) -> Rest(x, fun () -> sieve (streamfilter (fun k -> not (k mod x = 0)) (xf()) ))
  in 
  intstream 2 |> sieve |> (firstn n);;

let primes = getprimes 100;; 
