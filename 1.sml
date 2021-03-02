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

    fun fact 0 = 1
      | fact n = n * fact(n-1)
    fun pow (b,0) = 1
      | pow (b,1) = b
      | pow (b,n) = b * pow (b, n-1)
    fun double n = 2 * n
end;