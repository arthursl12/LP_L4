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

fun useMyMathLib (n, funct) =
  (case funct of
    "pow" => print ((Int.toString (MyMathLib.pow(n,n))) ^ " ")
  | "double" => print ((Int.toString (MyMathLib.double(n))) ^ " ")
  | "fact" => print ((Int.toString (MyMathLib.fact(n)))  ^ " ")
  | _ => raise Match)
  handle NegativoError => print "Não posso lidar com números negativos ";