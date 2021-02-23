(* 
TODO: 
    - Tratamento de exceções
    - Testes
*)

signature MATH =
sig
    type number = int
    val fact : number -> number
    val halfPi : real
    val pow : number * number -> number
    val double : number -> number
end ;

structure MyMathLib :> MATH =
struct
    type number = int
    val halfPi = Math.pi/2.0
    exception NegativoError

    fun fact 0 = 1
      | fact n = 
            if n < 0 then
                raise NegativoError
            else
               n * fact(n-1)
    fun pow (b,0) = 
            if b < 0 then 
               raise NegativoError 
            else 
               b
      | pow (b,n) = 
            if n < 0 orelse b < 0 then
                raise NegativoError
            else
               b + pow (b, n-1)
    fun double n = 2 * n
end;

exception AssertionError
fun assert (e1: ''a, expected: ''a) =
      if e1 <> expected then 
        raise AssertionError
      else
        true
;
fun assertR (e1,expected) =
   if (abs(e1 - expected) > 0.00001) then 
      raise AssertionError
   else
      true
;


MyMathLib.pow(2,3);
assert(MyMathLib.pow(2,3), 8);
assert(MyMathLib.pow(2,~3), 0.125);
