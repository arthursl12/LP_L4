signature MATH =
sig
    type number = int
    val fact : number -> number
    val halfPi : real
    val pow : number * number -> number
    val double : number -> number

    exception NegativoError
    exception ZeroToZero
end ;

structure MyMathLib :> MATH =
struct
    type number = int
    val halfPi = Math.pi/2.0
    exception NegativoError
    exception ZeroToZero


    fun fact 0 = 1
      | fact n = 
            if n < 0 then
                raise NegativoError
            else
               n * fact(n-1)
    fun pow (b,0) = 
            if b < 0 then 
               raise NegativoError 
            else if b = 0 then
                raise ZeroToZero
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