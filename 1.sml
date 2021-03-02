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
               1
      | pow (b,1) = 
            if b < 0 then
                raise NegativoError
            else
               b
      | pow (b,n) = 
            if n < 0 orelse b < 0 then
                raise NegativoError
            else
               b * pow (b, n-1)
    fun double n = 
            if n < 0 then
                raise NegativoError
            else
              2 * n
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



fun useMyMathLib (n, funct) =
  (case funct of
    "pow" => print ((Int.toString (MyMathLib.pow(n,n))) ^ " ")
  | "double" => print ((Int.toString (MyMathLib.double(n))) ^ " ")
  | "fact" => print ((Int.toString (MyMathLib.fact(n)))  ^ " ")
  | _ => raise Match)
  handle NegativoError => print "Não posso lidar com números negativos ";




MyMathLib.pow(2,3);
print "Pow\n";
assert(MyMathLib.pow(2,3), 8);
assert(MyMathLib.pow(2,0), 1);
assert(MyMathLib.pow(2,1), 2);
assert(MyMathLib.pow(1,1), 1);
assert(MyMathLib.pow(1,54), 1);
assert(MyMathLib.pow(0,54), 0);
assert(MyMathLib.pow(1,0), 1);
assert(MyMathLib.pow(0,0), 1);
assert(MyMathLib.pow(0,1), 0);
assert(MyMathLib.pow(0,28934), 0);

print "Double\n";
assert(MyMathLib.double(0), 0);
assert(MyMathLib.double(1), 2);
assert(MyMathLib.double(55), 110);

print "Fact\n";
assert(MyMathLib.fact(0), 1);
assert(MyMathLib.fact(1), 1);
assert(MyMathLib.fact(2), 2);
assert(MyMathLib.fact(3), 6);
assert(MyMathLib.fact(10), 3628800);

print "use - Pow\n";
useMyMathLib(~1, "pow");
useMyMathLib(0, "pow");
useMyMathLib(1, "pow");
useMyMathLib(5, "pow");

print "use - double\n";
useMyMathLib(5, "double");
useMyMathLib(0, "double");
useMyMathLib(~1, "double");

print "use - fact\n";
useMyMathLib(5, "fact");
useMyMathLib(0, "fact");
useMyMathLib(~1, "fact");
print "=============FIM DOS TESTES\n";




