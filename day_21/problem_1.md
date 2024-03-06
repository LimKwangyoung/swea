# 문제 1-2
다음 명제들이 항진명제라는 것을 진리표를 이용해서 보이시오.

|p|q|(~p$\vee$q)|(p$\wedge$~q)|(~p$\vee$q)$\vee$(p$\wedge$~q)|
|:-:|:-:|:-:|:-:|:-:|
|T|T|T|F|T|
|T|F|F|T|T|
|F|T|T|F|T|
|F|F|T|F|T|

# 문제 2-2
다음 명제들이 모순명제라는 것을 진리표를 이용해서 보이시오.

|p|q|(p$\wedge$q)|(p$\wedge$~q)|(p$\wedge$q)$\vee$(p$\wedge$~q)|
|:-:|:-:|:-:|:-:|:-:|
|T|T|T|F|F|
|T|F|F|T|F|
|F|T|F|F|F|
|F|F|F|F|F|

# 문제 3-2
다음 명제의 쌍 들에 대해서 두 명제가 동등한지를 진리표를 이용해 확인하시오.

|p|q|(~p$\vee$~q)|~(p$\vee$q)|
|:-:|:-:|:-:|:-:|
|T|T|F|F|
|T|F|T|F|
|F|T|T|F|
|F|F|T|T|

# 문제 4-2
명제식의 변형을 통하여 다음 명제를 간소화하시오.

(p$\vee$~q)$\wedge$(~p$\vee$~q) = ~q

# 문제 5-2
다음 명제들이 참인지 확인하시오.

$\forall x \in \Z, x^2 \geq x$ (True)

# 문제 5-4
다음 명제들이 참인지 확인하시오.

$\exist x \in \Z, x^2 < x$ (False)

# 문제 7
$n$이 홀수이면 $n^2+n$은 짝수임을 증명하라.

proof )  
$k \in Z$에 대해서 $n$은 홀수이므로, $n=2k-1$라고 하자.  
$n^2+n=(2k-1)^2+(2k-1)=(4k^2-4k+1)+(2k-1)=4k^2-6k+2=2(2k^2-3k+1)$  
$2k^2-3k+1 \in N$이므로 $n^2+n$은 짝수이다.

# 문제 9
자연수 $n$에 대해, $n^2+5$가 홀수이면 $n$은 짝수임을 증명하라.

proof )  
명제의 대우는 다음과 같다.  
자연수 $n$에 대해, $n$이 홀수이면 $n^2+5$은 짝수이다.  
$k \in N$에 대해서 $n$은 홀수이므로, $n=2k-1$라고 할 수 있다.  
$n^2+5=(2k-1)^2+5=(4k^2-4k+1)+5=4k^2-4k+6=2(2k^2-2k+3)$  
$2k^2-2k+3 \in N$이므로 $n^2+5$은 짝수이다.

# 문제 11
자연수 $n$에 대해 $n^2+5n+3$은 항상 홀수임을 증명하라.

proof )  
(1) $n$이 홀수일 경우  
$k \in N$에 대해서 $n=2k-1$라고 하자.  
$n^2+5n+3=(2k-1)^2+5(2k-1)+3=(4k^2-4k+1)+(10k-5)+3=4k^2+6k-1=2(2k^2+3k)-1$  
$2k^2+3k \in N$이므로 $n^2+5n+3$은 홀수이다.  
(2) $n$이 짝수일 경우  
$k \in N$에 대해서 $n=2k$라고 하자.  
$n^2+5n+3=(2k)^2+5\times2k+3=4k^2+10k+3=2(2k^2+5k)+1$  
$2k^2+5k \in N$이므로 $n^2+5n+3$은 홀수이다.