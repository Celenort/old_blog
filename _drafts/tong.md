# **분포에 관한 추론**

## 모분산에 관한 추론

-   모집단의 변동성(variability) 혹은 퍼짐(spread)의 정도에 관심이 있을
    경우 모분산이 추론의 대상이 됨.

-   모분산의 추정량 $\sigma^2$의 추정량인 표본분산을 이용할 수 있음.

-   $E(S^2) = \sigma^2$ 이므로,
    $$S^2 = {{\sum_{i=1}^n (X_i - \bar{X})^2}\over{n-1}}$$

-   카이제곱분포(chi-squared distribution) k개의 확률변수들이 N(0,1)의
    랜덤표본일 때 각 변수들의 제곱합의 분포를 자유도 k인 카이제곱
    분포라고 한다.

-   Theroem (정규모집단에서 표본분산의 분포) : 정규분포로부터의 랜덤
    표본이라 할 때 표본분산에 관한 식

    $${ {(n-1)S^2}\over{\sigma^2} } \sim {\chi^2(n-1)}$$

-   가정 : 모집단이 정규분포를 따름, 단순임의추출을 해야 함.

-   증명 : $X_i$ 들이 정규분포 $N(\mu, \sigma^2)$ 의 랜덤표본일 때,
    ${X_i-\mu}\over{\sigma}$ $\sim$ $N(0,1)$ 이고 서로 독립이므로,
    카이제곱 분포의 정의로부터
    ${\sum_{i=1}^n({{ {X_i-\mu}}\over{\sigma}})^2 } = \chi^2(n)$ 이며,
    $S^2$ 은 $\mu$가 아닌 $\bar{X}$ 로 빼서 구한 것이므로,
    ${\sum_{i=1}^n({{ {X_i-\mu}}\over{\sigma}})^2 }$ =
    ${\sum_{i=1}^n({{ {X_i-\bar{X}}}\over{\sigma}})^2 }$ +
    $n ({{\bar{X}-\mu}\over{\sigma}})^2$ 로 나눌 수 있으며, 적당히 수를
    곱하여 좌변은 $\chi^2(n)$을 따르고, 우변의 두번째 항은 $\chi^2(1)$
    이므로 카이제곱분포의 가법성에 의하여 위 공식이 성립한다.

-   카이제곱 분포의 분위수 : 자유도가 k인 카이제곱분포의 $1-\alpha$
    분위수를 $\chi_\alpha ^2(k)$ 로 나타내며, 즉 V $\sim$ $\chi^2 (k)$
    일 때 $P\{ V\geq \chi_\alpha ^2(k)\} = \alpha$

-   Theorem (카이제곱 분포의 가법성) : 각각의 카이제곱을 따르는 두
    변수가 서로 독립일 때 두 변수의 합은 각각의 자유도의 합을 자유도로
    하는 카이제곱분포와 같다.

-   모분산의 신뢰구간 : $\chi^2 (n-1)$의 $\alpha / 2$ 와 $1-\alpha / 2$
    백분위수를 이용하여 유의수준 $\alpha$의 신뢰구간
    $1-\alpha = P \{\chi_{1-\alpha /2} ^2 (n-1) \leq {\frac{(n-1) S ^2} {\sigma ^2} } \leq \chi_{\alpha /2} ^2 (n-1)  \}$
    $\sigma^2$로 정리하면 모분산에 대한 $100(1-\alpha) \%$ 신뢰구간은
    다음과 같다 :
    $\{\frac{(n-1) s^2}{\chi_{\alpha/2}^2 (n-1)}, \frac{(n-1) s^2}{\chi_{1-\alpha/2}^2 (n-1)}\}$

-   모분산의 가설 검정(정규모집단의 경우) : - 오른쪽 단측 검정의 경우
    $H_1 : \sigma^2 > \sigma_0 ^2$ , 유의확률
    $P = P(\chi^2 \geq \chi_0 ^2)$ 유의수준 $\alpha$ 의 기각역은
    $\chi_0 ^2 \geq \chi_\alpha ^2 (n-1)$ - 왼쪽 단측 검정의 경우
    $H_1 : \sigma^2 < \sigma_0 ^2$ , 유의확률
    $P = P(\chi^2 \leq \chi_0 ^2)$ 유의수준 $\alpha$ 의 기각역은
    $\chi_0 ^2 \leq \chi_{1-\alpha} ^2 (n-1)$ - 양측검정의 경우의
    유의확률은 $2P(\chi^2 \geq \chi_0^2)$ 와 $2P(\chi^2 \leq \chi_0^2)$
    중 1보다 작은 값을 유의확률로 계산하며, 유의수준 $\alpha$의 기각역은
    $\chi_0 ^2 \geq \chi_{\alpha /2} ^2 (n-1)$ or
    $\chi_0 ^2 \leq \chi_{1-\alpha /2} ^2 (n-1)$

## 두 모집단의 모평균의 비교

-   두 모집단의 모평균의 차이가 있는지를 검정. 귀무가설 :
    $H_0 : \mu_1 = \mu_2$, $H_1 : \mu_1 \neq \mu_2$

-   두 모평균 차의 추정치는 표본평균 차이다. 즉
    $\widehat{\mu_1 -\mu_2} = \bar{x_1}-\bar{x_2}$

-   두 모집단의 모평균 : $\mu_1, \mu_2$ , 모분산 :
    $\sigma_1^2, \sigma_2^2$, 표본수 : $n_1, n_2$ , 표본평균 :
    $\bar{x_1}, \bar{x_2}$, 표본분산 : $s_1^2 , s_2^2$

-   두 집단의 모평균 비교에서 필요한 가정사항 : (랜덤표본, 독립관측,
    각각 정규분포(CLT는 적용가능))

    1.  각 그룹에서의 관측값들은 각 모집단에서의 랜덤 표본이다.

    2.  서로 다른 그룹에서의 관측값들은 독립적으로 관측된 것이다.

    3.  두 모집단은 각각 정규분포를 따른다. (표본이 클 경우 무시될 수
        있음. (by, CLT)

-   랜덤화(randomization) : 각 처리를 적용할 실험단위를 랜덤하게 정하는
    과정.

-   $\bar{X_1}-\bar{X_2}$의 표본분포 : 모평균의 차의 추정치 : 모평균의
    차 표본평균의 차이의 분산과 표준편차 :
    $Var(\bar{X_1}-\bar{X_2}) = Var(\bar{X_1}) + Var(\bar{X_2}) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$
    (두 표본평균의 공분산 항이 0임, 독립성에 의해.)

-   두 모평균의 차이에 관한 추론 ($\sigma_1^2, \sigma_2^2$를 아는
    경우) - 두 모집단이 정규분포 : $\bar{X_1} - \bar{X_2}$를
    표준화시키면 표준정규분포를 따른다. - 두 모집단이 정규분포를 따르지
    않으면 : 표본수가 증가할수록 CLT에 따라 근사적으로 표준정규분포에
    가까워진다. - 검정통계량 :
    $Z = \frac{(\bar{X_1}-\bar{X_2}) - (\mu_1-\mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim{} N(0,1)$
    $\rightarrow$ 모평균을 알고 검증하는 꼴이므로 검정통계량이
    정규분포를 따르게 됨. - $\mu_1-\mu_2$ 에 대한 $100(1-\alpha)\%$
    신뢰구간 :
    $(\bar{X_1}-\bar{X_2}) \pm z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$ -
    유의확률과 기각역 : Z-검정을 그대로 따름. - 오른쪽 단측 검정의 경우,
    유의확률 $P = P(Z \geq z)$ 유의수준 $\alpha$ 의 기각역은
    $z\geq z_\alpha$ - 왼쪽 단측 검정의 경우, 유의확률 $P = P(Z\leq z)$
    유의수준 $\alpha$ 의 기각역은 $z\leq - z_\alpha$ - 양측검정의 경우,
    유의확률 $P=P(|Z| \geq |z|)$ 유의수준 $\alpha$의 기각역은
    $|z| \geq z_{\alpha /2}$

-   합동표본분산(pooled sample variance) : $S_p ^2$ 공동모분산
    $\sigma_2$의 추정량으로 각 표본분산의 자유도에 대한 가중평균으로
    정의 $S_p^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$ - pf)
    각각의 분포는 서로 독립이며, 각 분포에 대한 카이제곱 통계량
    $\frac{(n_1-1)S_1^2}{\sigma^2} \sim \chi^2(n_1-1)$ ,
    $\frac{(n_2-1)S_2^2}{\sigma^2} \sim \chi^2(n_2-1)$ 에서 카이제곱
    분포의 가법성에 의해..

-   두 모평균의 차이에 대한 추론($\sigma_1^2, \sigma_2^2$을 모르는 경우,
    두 모분산이 같다는 등분산 가정이 있을 때, 정규분포 모집단 가정) -
    표본평균의 차에 대한 분산 추정 :
    $\widehat{Var}(\bar{X_1}-\bar{X_2}) = \frac{\hat{\sigma_1}^2}{n_1} + \frac{\hat{\sigma_2}^2}{n_2}=\frac{\sigma^2}{n_1} + \frac{\sigma^2}{n_2} = S_p^2 (n_1^{-1} + n_2^{-1})$ -
    추정된 분산으로 표준화한 통계량은 자유도 ($df = n_1-n_2-2$) 인 t
    분포를 따르게 됨 $\rightarrow$ 모평균을 모르고 검증하는 꼴이므로
    검정통계량이 t분포를 따르게 됨. - 검정통계량 T =
    $\frac{(\bar{X_1}-\bar{X_2}) - (\mu_1-\mu_2)}{S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim{} t_{(n_1+n_2-2)}$ -
    증명 : $\frac{(n_1+n_2-2)S_p^2}{\sigma^2} \sim{}\chi_2(n_1+n_2-2)$,
    t분포의 정의($N(0,1) / \chi_2(n_1+n_2-2) \sim{} t(n_1+n_2-2)$ )
    사용 - $\mu_1 - \mu_2$ 에 대한 $100(1-\alpha) \%$ 신뢰구간 :
    $(\bar{X_1}-\bar{X_2}) \pm t_{\alpha/2}(n_1+n_2-2) S_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$ -
    오른쪽 단측 검정의 경우, 유의확률 $P = P(T \geq t)$ 유의수준
    $\alpha$ 의 기각역은 $t\geq t_\alpha(n_1+n_2-2)$ - 왼쪽 단측 검정의
    경우, 유의확률 $P = P(T\leq t)$ 유의수준 $\alpha$ 의 기각역은
    $t\leq - t_\alpha(n_1+n_2-2)$ - 양측검정의 경우, 유의확률
    $P= P(|T| \geq |t|)$ 유의수준 $\alpha$의 기각역은
    $|t| \geq t_{\alpha /2}(n_1+n_2-2)$

-   두 모평균의 차이에 대한 추론($\sigma_1^2, \sigma_2^2$을 모르는 경우,
    두 모분산이 같다는 등분산 가정이 있을 때, 정규분포는 아니지만
    대표본인 경우) - 검정통계량은 근사적으로 표준정규분포를 따르게 됨.
    (by CLT) - 검정통계량 Z =
    $\frac{(\bar{X_1}-\bar{X_2}) - (\mu_1-\mu_2)}{S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \dot\sim N(0,1)$ -
    대표본($n_1, n_2 \geq 30$)

-   두 모평균의 차이에 대한 추론 ($\sigma_1^2, \sigma_2^2$을 모르는
    경우, 두 모분산이 다를 때 (이분산) , 정규분포 모집단 가정) -
    표본평균의 차에 대한 분산 추정 :
    $\widehat{Var}(\bar{X_1}-\bar{X_2}) = \frac{\hat{\sigma_1}^2}{n_1} + \frac{\hat{\sigma_2}^2}{n_2}=\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}$ -
    추정된 분산으로 표준화한 통계량은 자유도 ($df$) 인 t 분포를 따르게
    됨 $\rightarrow$ 모평균을 모르고 검증하는 꼴이므로 검정통계량이
    t분포를 따르게 됨. -
    $df = \frac{(\frac{S_1^2}{n_1}+ \frac{S_2^2}{n_2})^2}{\frac{(\frac{S_1^2}{n_1})^2}{n_1-1} + \frac{(\frac{S_2^2}{n_2})^2}{n_2-1}}$ -
    검정통계량 T =
    $\frac{(\bar{X_1}-\bar{X_2}) - (\mu_1-\mu_2)}{\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}} \dot\sim{} t_{(df)}$ -
    $\mu_1 - \mu_2$ 에 대한 $100(1-\alpha) \%$ 신뢰구간 :
    $(\bar{X_1}-\bar{X_2}) \pm t_{\alpha/2}(df) \sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}$ -
    오른쪽 단측 검정의 경우, 유의확률 $P = P(T \geq t)$ 유의수준
    $\alpha$ 의 기각역은 $t\geq t_\alpha(df)$ - 왼쪽 단측 검정의 경우,
    유의확률 $P = P(T\leq t)$ 유의수준 $\alpha$ 의 기각역은
    $t\leq - t_\alpha(df)$ - 양측검정의 경우, 유의확률
    $P= P(|T| \geq |t|)$ 유의수준 $\alpha$의 기각역은
    $|t| \geq t_{\alpha /2}(df)$

-   두 모평균의 차이에 대한 추론 ($\sigma_1^2, \sigma_2^2$을 모르는
    경우, 두 모분산이 다를 때 (이분산) ,정규분포는 아니지만 대표본인
    경우) - 추정된 분산으로 표준화한 통계량은 CLT에 의해 표준정규분포를
    따르게 됨. - 검정통계량 Z =
    $\frac{(\bar{X_1}-\bar{X_2}) - (\mu_1-\mu_2)}{\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}} \dot\sim{} N(0,1)$ -
    대표본($n_1, n_2 \geq 30$) - $\mu_1 - \mu_2$ 에 대한
    $100(1-\alpha) \%$ 신뢰구간 :
    $(\bar{X_1}-\bar{X_2}) \pm z_{\alpha/2} \sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}$ -
    오른쪽 단측 검정의 경우, 유의확률 $P = P(Z \geq z)$ 유의수준
    $\alpha$ 의 기각역은 $z\geq z_\alpha$ - 왼쪽 단측 검정의 경우,
    유의확률 $P = P(Z\leq z)$ 유의수준 $\alpha$ 의 기각역은
    $z\leq - z_\alpha$ - 양측검정의 경우, 유의확률 $P= P(|Z| \geq |z|)$
    유의수준 $\alpha$의 기각역은 $|z| \geq z_{\alpha /2}$

-   선형 보간법 : ex) df = 7.8 이면 df=7과 df 8을 가중평균하여 그 값을
    이용함. but 시험에서는 가까운 값으로 이용.

## 대응비교에 의한 모평균의 비교

-   두 모집단의 평균을 비교할 때 동질적인 비교 대상들로 쌍을 이루어 각
    쌍 내에서 차를 이용해 비교하는 방법

-   개체간의 이질성을 감안하여야 함. 일반적인 모평균의 비교에서는
    독립이라는 가정 만족 못하므로, 두 측정값의 차를 이용해 추론하면 됨.

-   주어진 자료 : $(X_1, Y_1), \cdots (X_n, Y_n)$ 에서 측정값의 차
    $d_i = X_i-Y_i$ (i = 1, 2, \..., n)

-   가정사항 : 개체의 각 특성값의 차가 정규분포로부터의 랜덤표본의 가정,
    표본크기 n이 충분히 크면 근사적 성립.

-   $E(d_i) = \mu_1 - \mu_2 = \mu_D$ ,
    $S_D^2 = \frac{1}{n-1} \sum (d_i-\bar{d}) ^2$

-   모평균 $\mu_D$의 추정량 표본평균 $\bar{D}$, 불편추정량이며
    표본평균의 분산 $Var(\bar{D}) = \frac{s_D^2}{n}$

-   대응평균에 의한 모평균의 비교 방법
    -$H_0 : \mu_1 - \mu_2 = \mu_D = 0$ 에 대한 검정통계량 -
    $T = \frac{\bar{D}-\mu_D}{\sqrt{\frac{S_D^2}{n}}} \sim t_{n-1}$ -
    $\mu_1 - \mu_2$에 대한 $100(1-\alpha)\%$ 신뢰구간 :
    $\bar{d} \pm t_{\alpha/2} (n-1) \sqrt{\frac{s_D^2}{n}}$ - 오른쪽
    단측 검정의 경우, 유의확률 $P = P(T \geq t)$ 유의수준 $\alpha$ 의
    기각역은 $t\geq t_\alpha(n-1)$ - 왼쪽 단측 검정의 경우, 유의확률
    $P = P(T\leq t)$ 유의수준 $\alpha$ 의 기각역은
    $t\leq - t_\alpha(n-1)$ - 양측검정의 경우, 유의확률
    $P= P(|T| \geq |t|)$ 유의수준 $\alpha$의 기각역은
    $|t| \geq t_{\alpha /2}(n-1)$

-   등분산 이표본의 비교와 대응비교의 분석 - 주어진 자료에서 총 자료의
    갯수 : n , $\sigma_X^2, \sigma_Y^2$ 의 값은 모른다고 가정. - 등분산
    이표본 :
    $T= \frac{(\bar{X_1}-\bar{X_2}) - (\mu_1-\mu_2)}{S_p \sqrt{\frac{1}{n} + \frac{1}{n}}} \sim{} t_{(2n-2)}$ -
    대응비교 :
    $T = \frac{\bar{D}-\mu_D}{\sqrt{\frac{S_D^2}{n}}} \sim t_{n-1}$ -
    분자는 동일하나, $\bar{X}, \bar{Y}$가 양의 상관관계를 보인다면
    $Var(\bar{X}-\bar{Y})$ 가 작아져 검정통계량 값이 커져 대응비교에서의
    귀무가설 기각이 편해짐. - t분포의 자유도 측면에서는 등분산 이표본이
    $2n-2$, 대응비교가 $n-1$로 동일 조건에서 대응비교의 귀무가설 기각이
    더 힘들어짐(대응비교의 penalty) - 실험단위들이 이질적, 각 쌍 내에서
    값들이 양의 상관관계 가지면 대응비교, 그렇지 않으면 등분산 이표본의
    비교가 나음.

## 두 모비율의 차이에 대한 추론

-   두 모집단에서 $n_1, n_2$개의 랜덤표본의 독립적 추출, 해당 속성이
    $X_1, X_2$개 나타남. $X_1, X_2$는 각각 $B(n_1, p_1), B(n_2, p_2)$를
    따름.

-   두 모비율 차의 추정량 :
    $\widehat{p_1-p_2} = \hat{p_1}-\hat{p_2} = \frac{X_1}{n_1} - \frac{X_2}{n_2}$

-   기댓값 : 불편추정량이며, 분산 :
    $Var(\widehat{p_1-p_2}) = \frac{p_1(1-p_1)}{n_1}+\frac{p_2(1-p_2)}{n_2}$

-   표본크기들이 모두 충분히 큰 경우,
    $\hat{p_1} \dot\sim N(p_1, \frac{p_1(1-p_1)}{n_1})$ ,
    $\hat{p_2} \dot\sim N(p_2, \frac{p_2(1-p_2)}{n_2})$ 에서 각각
    독립이므로,
    $\hat{p_1}-\hat{p_2} \dot\sim N(p_1-p_2, \frac{p_1(1-p_1)}{n_1}+\frac{p_2(1-p_2)}{n_2})$
    가 성립함. n이 크다는 것의 기준은 np, n(1-p)가 모두 5 이상.

-   두 모비율에 차에 대한 $100(1-\alpha) \%$ 신뢰구간
    $((\hat{p_1}-\hat{p_2} )-z_{\alpha/2}\hat{SE}(\widehat{p_1-p_2}),(\hat{p_1}-\hat{p_2} )+z_{\alpha/2}\hat{SE}(\widehat{p_1-p_2}))$

-   두 모비율의 비교를 위한 검정 - 귀무가설 $H_0 : p_1 = p_2$ 일 때 두
    모집단에서의 공통 모비율, 즉 합동표본비율
    $\hat{p} = \frac{X_1+X_2}{n_1+n_2}$ - 분산
    $Var(\hat{p_1}-\hat{p_2}) = p(1-p) (\frac{1}{n_1}+\frac{1}{n_2})$
    이므로 분산의 추정량
    $\widehat{Var}(\hat{p_1}-\hat{p_2}) = \hat{p}(1-\hat{p}) (\frac{1}{n_1}+\frac{1}{n_2})$ -
    검정통계량
    $Z = \frac{\hat{p_1}-\hat{p_2}}{\sqrt{\hat{p}(1-\hat{p}) (\frac{1}{n_1}+\frac{1}{n_2})}} \dot\sim N(0,1)$ -
    오른쪽 단측 검정의 경우, 유의확률 $P = P(Z \geq z)$ 유의수준
    $\alpha$ 의 기각역은 $z\geq z_\alpha$ - 왼쪽 단측 검정의 경우,
    유의확률 $P = P(Z\leq z)$ 유의수준 $\alpha$ 의 기각역은
    $z\leq - z_\alpha$ - 양측검정의 경우, 유의확률 $P= P(|Z| \geq |z|)$
    유의수준 $\alpha$의 기각역은 $|z| \geq z_{\alpha /2}$

## 두 모집단의 분산에 관한 추론

-   두 모집단 분산 비교 : 두 모평균 비교시 등분산 가정의 적합성 분석

-   두 모집단의 표준편차 $\sigma_1, \sigma_2$ 비교, 그 비율이 1이 되면
    두 분산/표준편차가 같다고 간주.

-   모분산 비율($\frac{\sigma_1^2}{\sigma_2^2}$)에 관한 점추정량 :
    $\frac{s_1^2}{s_2^2}$

-   모분산 비율에 대한 추론 :
    $\frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2} \sim F(n_1-1, n_2-1)$

-   F 분포 : $V_1, V_2$가 서로 독립이고 각각 자유도가 $k_1, k_2$인
    카이제곱 분포를 따를 때 $F = \frac{V_1/k_1}{V_2/k_2}$를 자유도
    $(k_1, k_2)$ 인 F 분포라고 함.

-   F 분포의 분위수 : $P\{F\geq F_\alpha(k_1, k_2)\} = \alpha$ 일 때 이
    값을 F분포의 $1-\alpha$분위수라고 부름.

-   F 분포의 특징 :
    $\frac{1}{F} \sim F(k_2, k_1)  \rightarrow F_{1-\alpha} (k_2, k_1) = \frac{1}{F_\alpha(k_1, k_2)}$

-   F분포와 T 분포와의 관계 : 확률변수 T가 자유도 k인 t분포를 따를 때
    $T^2 \sim F(1,k)$ - pf ) $T = \frac{Z}{\sqrt{V/k}}$ 이고 분자 분모가
    서로 독립이므로, 양변 제곱하면 $Z^2 \sim \chi^2(1)$ 이므로 QED

-   모분산의 비교시 가정 :

    1.  두 모집단이 정규분포를 따름.

    2.  표본 추출 시 독립적인 단순임의추출 필요

-   모분산의 비에 관한 $100(1-\alpha) \%$ 신뢰구간 :
    $(\frac{s_1^2}{s_2^2} / F_{\alpha/2} (n_1-1, n_2-1), \frac{s_1^2}{s_2^2} \cdot F_{\alpha/2} (n_2-1, n_1-1))$ -
    오른쪽 단측 검정의 경우 $H_1 : \sigma_1^2 > \sigma_2 ^2$ , 유의확률
    $P = P(F \geq f)$ 유의수준 $\alpha$ 의 기각역은
    $f \geq F_\alpha (n_1-1, n_2-1)$ - 왼쪽 단측 검정의
    경우$H_1 : \sigma_1^2 < \sigma_2 ^2$ , 유의확률 $P = P(F \leq f)$
    유의수준 $\alpha$ 의 기각역은$f \leq 1/F_\alpha (n_2-1, n_1-1)$ -
    양측검정의 경우의 유의확률은 $2P(F \geq f)$ 와 $2P(F \leq f)$ 중
    1보다 작은 값을 유의확률로 계산하며, 유의수준 $\alpha$의 기각역은
    $f \geq F_{\alpha/2} (n_1-1, n_2-1)$
    $f \leq 1/F_{\alpha/2} (n_2-1, n_1-1)$

# 이산자료의 분석

## 다항모집단의 동질성검정

-   다항모집단 : 각 모집단이 세 가지 이상의 서로 다른 속성 갖는 개체들로
    나뉘는 경우 ($c\geq 3$) (이항모집단 : 두 가지의 서로 다른 속성)

-   귀무가설 $H_0 :$ 모집단 간의 분포가 동일 :
    $H_0 : p_{1j} = p_{2j} = \cdots p_{rj} (j = 1, 2, \cdots c)$
    대립가설 $H_1 :$ 이들이 서로 다르다. 각 범주의 관측도수가 귀무가설
    하에서의 추정 기대도수와 차이가 크면 귀무가설 기각.

-   추정 기대도수(estimated expected frequency) : $\hat{E}_{ij} =$ (표본
    크기 ) $\times$ ($H_0$ 하에서의 추정 확률 $=\hat{p_j}$ )
    $= \frac{O_{\cdot i }O_{i \cdot}}{n}$ ($O_{\cdot j }$ : j 범주에
    해당하는 도수의 합, $O_{i \cdot }$: i번째 모집단 도수의 합, $n_i$)
    $\hat{p_j} = \frac{O_{\cdot j}}{n}$ ( 범주 j에서 공통 모비율의
    추정값)

-   관측도수 $O_{ij}$와 추정 기대도수$\hat{E}_{ij}$ 의 차이를 나타내는
    검정통계량이 카이제곱통계량이며, 이 값은
    $\chi^2  = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij}-\hat{E}_{ij})^2}{\hat{E}_{ij}} \dot\sim \chi^2 ((r-1)(c-1))$

-   단측검정 : 검정의 기각역 $\chi_0^2 \geq \chi_{\alpha}^2((r-1)(c-1))$
    , 유의확률 $P = P(\chi^2\geq\chi_0^2)$

-   검정 조건 : 표본크기가 큰 경우 ( $\hat{E}_{ij} \geq 5$)

## 범주형 자료의 독립성 검정

-   독립성 검정(test of independence) : 두 변수가 독립인지 검정

-   두 특성 A, B가 서로 독립일 경우 $p_{ij} = p_{i\cdot}p_{\cdot j}$ 이
    성립하므로, 귀무가설 $H_0 : p_{ij} = p_{i\cdot}p_{\cdot j}$,
    대립가설 $H_1 : not H_0$

-   귀무가설 하에서의 (i, j) 칸의 모비율의 추정 :
    $\hat{p}_{ij} = \hat{p}_{i \cdot}\hat{p}_{\cdot j} = (\frac{O_{i \cdot}}{n})(\frac{O_{\cdot j}}{n})$
    , 추정 기대도수
    $\hat{E}_{ij} = n\hat{p}_{i \cdot}\hat{p}_{\cdot j} = (\frac{O_{i \cdot}O_{\cdot j} }{n})$

-   관측도수 $O_{ij}$와 추정 기대도수$\hat{E}_{ij}$ 의 차이를 나타내는
    검정통계량이 카이제곱통계량이며, 이 값은
    $\chi^2  = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij}-\hat{E}_{ij})^2}{\hat{E}_{ij}} \dot\sim \chi^2 ((r-1)(c-1))$

-   관측도수 $O_{ij}$와 추정 기대도수$\hat{E}_{ij}$ 의 차이를 나타내는
    검정통계량이 카이제곱통계량이며, 이 값은
    $\chi^2  = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij}-\hat{E}_{ij})^2}{\hat{E}_{ij}} \dot\sim \chi^2 ((r-1)(c-1))$

-   단측검정 : 검정의 기각역 $\chi_0^2 \geq \chi_{\alpha}^2((r-1)(c-1))$
    , 유의확률 $P = P(\chi^2\geq\chi_0^2)$

-   검정 조건 : 표본크기가 큰 경우 ( $\hat{E}_{ij} \geq 5$)

# 상관분석과 회귀분석

-   상관 분석(correlation analysis) : 두 변수간의 관계 유무 또는 관계
    강도에 대한 통계적 분석방법. 표본상관계수 r을 이용해 모상관계수
    $\rho$에 관한 추론

-   회귀분석(regression analysis) : 두 변수 사이의 함수 관계에 대한
    통계적 분석, 한 변수의 값으로부터 다른 변수의 값에 대한 예측

## 상관 분석

-   모상관계수 $\rho$ : 각 개체의 두가지 특성을 변수 X, Y로 나타낼 때 두
    변수 사이의 직선관계의 정도를 나타냄. 항상 $-1 \leq \rho \leq 1$.

-   표본상관계수 r : 모상관계수의 추정값으로 사용, 랜덤표본으로부터 두
    특성에 대한 자료가 n개의 쌍으로 주어지면,
    $r = \frac{\sum_{i=1}^n (x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i=1}^n (x_i-\bar{x})^2} \sqrt{\sum_{i=1}^n (y_i-\bar{y})^2}} = \frac{\sum_{i=1}^n x_i y_i-n\bar{x}\bar{y}}{\sqrt{\sum_{i=1}^n (x_i)^2-n\bar{x}^2} \sqrt{\sum_{i=1}^n (y_i)^2-n\bar{y}^2}}$
    이며, 항상 $-1 \leq r \leq 1$ 만족.

-   $r \sim 0$ 인 것은 두 변수간 직선관계가 약함을 의미, not 아무 관계가
    없는 것.,

-   $100r \%$ 의 선형 관계가 있으며 x에 의해서 y의 변량 중 $76\%$를
    설명할 수 있다고 말할 수 있음.

-   상관의 성질과 정도만을 의미하며, 변수간의 관계를 인과적으로
    설명하지는 X

-   상관관계의 유무에 관한 검정 - 표본상관계수 r을 이용하여 모상관계수
    $\rho$를 추론. - 가정사항 : 이변량정규모집단. - 귀무가설
    $H_0 : \rho = 0$ 에 대한 검정통계량
    $T = \sqrt{n-2} \frac{r}{\sqrt{1-r^2}}$ - 오른쪽 단측 검정의 경우,
    유의확률 $P = P(T \geq t) ,  T \sim t(n-2)$ 유의수준 $\alpha$ 의
    기각역은 $t\geq t_\alpha(n-2)$ - 왼쪽 단측 검정의 경우, 유의확률
    $P = P(T\leq t), T \sim t(n-2)$ 유의수준 $\alpha$ 의 기각역은
    $t\leq - t_\alpha(n-2)$ - 양측검정의 경우, 유의확률
    $P= P(|T| \geq |t|), T \sim t(n-2)$ 유의수준 $\alpha$의 기각역은
    $|t| \geq t_{\alpha /2}(n-2)$

## 단순선형회귀 분석

-   두 변수 사이의 함수관계를 파악하여 한 변수의 값으로부터 다른 변수의
    값 예측 ex) $Y = f(X)$

-   단순선형회귀분석(simple linear regression analysis) : 두 변수 사이의
    일차함수 관계, 즉 직선관계를 모형으로 하여 분석.

-   다중회귀분석 (multiple regression analysis) : 두 개 이상의 변수가 한
    변수에 영향을 줄 때, 한 변수를 여러 변수의 함수로 나타내어 분석.

-   설명변수(explanatory variable) : x, 다른 변수에 영향을 주는 변수로,
    예측변수 혹은 독립변수라고도 부름.

-   반응변수(response variable) : Y : 설명에 영향을 받는 변수, 종속변수

-   단순선형회귀모형 (simple linear regression model) - Model :
    $Y_i = \alpha + \beta x_i + \epsilon_i (i=1, 2, \cdots, n)$ $x_i$ :
    독립변수, 설명변수로 확률변수가 아닌 주어진 상수값임. $\epsilon_i$ :
    평균이 0, 분산이 $\sigma^2$인 오차항을 나타내는 확률변수. $\alpha$ :
    미지의 모수, y축의 절편으로 x=0일 때의 y의 값. $\beta$ : 미지의
    모수, 기울기, x 1단위 증가시 y의 변동량 - 단순선형회귀식
    $E(Y_i|x_i) = \alpha + \beta x_i$ 오차항 :
    $\epsilon_i = E(Y_i|x_i)-y_i$ - 오차항의 가정사항 :
    $\epsilon_i \sim_{i.i.d} N(0, \sigma^2)$ , $\epsilon_i$ 는 $Y_i$와
    그 평균 $E(Y_i|x_i)$ 간의 편차 , 각각의 오차항은 독립적으로 관측됨.

    1.  $E(\epsilon_i) = 0$ : 평균이 0

    2.  $Var(\epsilon_i) = \sigma^2 > 0$ : 등분산성

    3.  $\epsilon_i, \epsilon_j (for all i, j; i\neq j)$ 가 독립 :
        독립성

    4.  $\epsilon_i$ 가 정규분포를 따름 : 정규성

    \- 오차항의 가정사항으로 인해 반응변수가 따르는 가정사항 :
    $Y_i \sim_{i.i.d} N(\alpha+\beta x_i , \sigma^2)$

    1.  $E(Y_i|x_i) = \alpha+\beta x_i$

    2.  $Var(Y_i) = \sigma^2$

    3.  $Cov(Y_i, Y_j) = 0$

    4.  $Y_i$ 또한 정규분포를 따름

    \- 모회귀계수 ($\alpha, \beta$의 추정) : 최소제곱법, 오차의 제곱합
    $\sum_{i=1}^n \epsilon_i^2$를 최소로 하는 값을 그 추정값으로 한다.
    각각의 회귀계수에 대해 편미분하여 0이 되도록 하는 값을 정리 -
    $\hat{\beta} = \frac{S_{XY}}{S_{XX}}$,
    $\hat{\alpha} = \bar{y}-\hat{\beta}\bar{x}$ 이렇게 얻은 추정량을
    최소제곱 추정량이라고 부르며, $\hat{y} = \hat{\alpha}+ \hat{\beta}x$
    를 최소제곱 회귀직선이라 부름. - 종속변수
    $y_i = \alpha + \beta x_i + \epsilon_i = E(y_i|x_i) + \epsilon_i$(
    ideal model) /
    $y_i = \hat{\alpha} + \hat{\beta} x_i + e_i = \hat{y_i} + e_i$
    (based on data estimates) - $\epsilon_i$ : 이상적 관측값과 실제 값의
    차이 / $e_i$ : 회귀직선에 의한 추측값과 실제 값의 차이

-   잔차 (residual) - 설명변수 $x_i$ 에 대응되는 추측값
    $\hat{y_i} = \hat{\alpha} + \hat{\beta}x_i$ 와 실제 관측값 $y_i$의
    차이이며, 오차항 $\epsilon_i = y_i - E(y_i|x_i)$ 들의 관측값. -
    잔차를 통한 오차분산의 추정 :
    $SSE = \sum_{i=1}^n e_i^2 = \sum_{i=1}^n (y_i-\hat{y_i})^2$ SSE :
    error sum of squares / - 오차제곱합을 자유도로 나누어
    평균제곱오차(mean squared error, MSE 가 $\sigma^2$의 불편추정량임.
    $MSE = \frac{SSE}{df} = \frac{1}{n-2} \sum_{i=1}^n (y_i-\hat{y_i})^2$ -
    $SSE = S_{yy} - \hat{\beta}^2 S_{xx} = S_{yy} - \frac{S_{xy}^2}{S_{xx}}$

-   제곱합의 분해 (decomposition) : 반응변수의
    관측값($y_1, y_2, \cdots , y_n)$ 이 평균인 $\bar{y}$ 와 떨어진
    정도를 두 편차의 합으로 나타냄. - $y_i - \bar{y}$ (총 편차, total
    deviation) = $y_i - \bar{y_i}$ (잔차로써 오차항에 기인하는 편차) +
    $\hat{y_i} - \bar{y}$ (설명변수 x를 고려한, 회귀직선에 의해 설명되는
    오차) - SST(total sum of squares)$\sum_{i=1}^2(y_i-\bar{y})^2$ =
    SSE(error sum of squares) $\sum_{i=1}^2 (y_i-\hat{y_i})^2$+
    SSR(regression sum of squares)
    $\sum_{i=1}^2(\hat{y_i} - \bar{y})^2$ - SST : df=n-1 (n개의 자료,
    $\bar{y}$ 라는 1개의 restriction), SSE : df=n-2 (n개의 자료,
    $\hat{\alpha}, \hat{\beta}$라는 2개의 restriction), SSR : df = 1
    ($\hat{\alpha}, \hat{\beta}$ 에서 $\sum (\hat{y_i} - \bar{y}) = 0$ )

-   평균제곱과 제곱합, 결정계수 - 평균제곱 : 제곱합을 $df$로 나누어준 것
    : MSE = SSE / n-2 , MSR = SSR / 1 - $SST = S_{yy}$ - 결정계수
    $R^2 = \frac{SSR}{SST}  =1-\frac{SSE}{SST}$ : 총제곱합에서
    회귀제곱합으로 설명할 수 있는 비율이며, 결정계수는 표본상관계수의
    제곱값이다. - $R^2 \%$ 만큼 전체 자료의 산포 중 회귀직선이 설명해줌.

-   단순 회귀분석에서 회귀직선의 유의성에 대한 추론과 검정 (단순선형
    회귀모형의 가정사항 하에서) , 총체적 검정인 F 검정 - 귀무가설
    $H_0 : \beta = 0$ while 대립가설 $H_1 : \beta \neq 0$ - 검정통계량
    $F = \frac{SSR/1}{SSE / (n-2)} \sim F(1, n-2)$ (by Cochran's
    Theorem) - 유의확률 $P = P\{F\geq f\},  F \sim F(1, n-2)$ 이고,
    유의수준 $\alpha$ 의 기각역은 $f\geq F_\alpha (1, n-2)$ 인 오른쪽
    단측검정.

-   단순 회귀분석에서 기울기 $\beta$ 에 대한 추론, 모회귀계수 하나에
    대한 t검정 - 모회귀계수 $\beta$ 의 최소제곱추정량
    $\hat{\beta} = \frac{S_{xy}}{S_{xx}}  = \frac{\sum_{i=1}^n (x_i-\bar{x}) \cdot y_i}{\sum_{i=1}^n (x_i-\bar{x})^2}$
    이며,
    $E(\hat{\beta}) = \beta , Var{\hat{\beta}} = \frac{\sigma^2}{S_{xx}}$
    이므로, 독립적으로 정규분포를 따르는 $y_i$의 선형결합인
    $\hat{\beta}$ 도 정규분포 따름. ($x_i$는 상수)
    $\hat{\beta} \sim N(\beta,\frac{\sigma^2}{S_{xx}})$ - $\sigma^2$
    값을 모르면 $\hat{\sigma}^2$ 이라는 불편추정량으로 그 값 대체 가능.
    $s^2(\hat{\beta} ) = \widehat{Var}(\hat{\beta}) = \frac{\hat{\sigma}^2}{S_{xx}}$ -
    $\frac{\hat{\beta}- \beta}{\sqrt{Var(\hat{\beta})}} =\frac{\hat{\beta}- \beta}{\sqrt{\frac{\hat{\sigma}^2}{S_{xx}}}} \sim t(n-2)$
    : pf ) $T = \frac{N}{\sqrt{V/k}}$ 이므로, 이를 만족시킴. - $\beta$에
    대한 $100(1-\alpha) \%$ 신뢰구간 :
    $\hat{\beta} \pm t_{\alpha/2}(n-2) \sqrt{\frac{\hat{\sigma}^2}{S_{xx}}}$ -
    $H_0 : \beta = b$ 이며, 귀무가설 하에서 검정통계량
    $T = \frac{\hat{\beta}-b}{\sqrt{\frac{\hat{\sigma}^2}{S_{xx}}}} \sim t(n-2)$ -
    오른쪽 단측 검정의 경우, 유의확률 $P = P(T \geq t) ,  T \sim t(n-2)$
    유의수준 $\alpha$ 의 기각역은 $t\geq t_\alpha(n-2)$ - 왼쪽 단측
    검정의 경우, 유의확률 $P = P(T\leq t), T \sim t(n-2)$ 유의수준
    $\alpha$ 의 기각역은 $t\leq - t_\alpha(n-2)$ - 양측검정의 경우,
    유의확률 $P= P(|T| \geq |t|), T \sim t(n-2)$ 유의수준 $\alpha$의
    기각역은 $|t| \geq t_{\alpha /2}(n-2)$ - 회귀직선의 유의성 t 검정은,
    분산분석표를 이용한 F 검정으로도 할 수 있으며
    $F = \frac{SSR/1}{SSE/n-2} = \frac{\hat{\beta}^2S_{xx}}{MSE} = (\frac{\hat{\beta} - 0}{\sqrt{\frac{\hat{\sigma}^2}{S_{xx}}}})^2  = T^2$
    이므로, $t_{n-2}^2 = F(1, n-2)$ 의 관계가 있음을 알 수 있다.

-   유의성 F 검정과 T 검정의 비교 - F 검정은 모든 기울기 모수에 대한
    총체적 검정($overall test$ ) 를 수행 - 일반적으로 절편 $\alpha$ 는 F
    검정에서 제외한다. - 단순회귀모형에서는 $\alpha$ 제외한 회귀계수가
    $\beta$ 하나이므로 t 검정과 F 검정의 결과가 완전히 동일하며,
    검정통계량 끼리는 $t^2 = F$ 라는 관계가 있다.

-   절편 $\alpha$ 에 관한 추론 - 모회귀계수 $\beta$ 의 최소제곱추정량
    $\hat{\alpha} = \bar{y} - \hat{\beta}\bar{x} = \sum_{i=1} ^2 \frac{y_i}{n} - \frac{\sum_{i=1}^n (x_i-\bar{x}) \cdot y_i}{\sum_{i=1}^n (x_i-\bar{x})^2} \bar{x}$
    이며,
    $E(\hat{\alpha}) = \alpha , Var({\hat{\alpha}}) = \sigma^2(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}})$
    이므로, 독립적으로 정규분포를 따르는 $y_i$의 선형결합인
    $\hat{\alpha}$ 도 정규분포 따름. ($x_i$는 상수)
    $\hat{\alpha} \sim N(\alpha,\sigma^2(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}))$ -
    $\sigma^2$ 값을 모르면 $\hat{\sigma}^2$ 이라는 불편추정량으로 그 값
    대체 가능.
    $s^2(\hat{\alpha} ) = \widehat{Var}(\hat{\alpha}) = \hat{\sigma}^2(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}})$ -
    $\frac{\hat{\alpha}- \alpha}{\sqrt{Var(\hat{\alpha})}} =\frac{\hat{\beta}- \beta}{\sqrt{\frac{\hat{\sigma}^2}{S_{xx}}}} \sim N(0, 1)$
    or $t(n-2)$ : $\sigma^2$ 을 알 때와 모를 때 각각 정규분포, t-분포를
    따름. - $\alpha$에 대한 $100(1-\alpha) \%$ 신뢰구간($\sigma^2$ 모를
    때) :
    $\hat{\alpha} \pm t_{\alpha/2}(n-2) \sqrt{\hat{\sigma}^2(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}})}$ -
    $H_0 : \alpha = a$ 이며, 귀무가설 하에서 검정통계량
    $T = \frac{\hat{\alpha}-a}{\sqrt{\hat{\sigma}^2(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}})}} \sim t(n-2)$ -
    오른쪽 단측 검정의 경우, 유의확률 $P = P(T \geq t) ,  T \sim t(n-2)$
    유의수준 $\alpha$ 의 기각역은 $t\geq t_\alpha(n-2)$ - 왼쪽 단측
    검정의 경우, 유의확률 $P = P(T\leq t), T \sim t(n-2)$ 유의수준
    $\alpha$ 의 기각역은 $t\leq - t_\alpha(n-2)$ - 양측검정의 경우,
    유의확률 $P= P(|T| \geq |t|), T \sim t(n-2)$ 유의수준 $\alpha$의
    기각역은 $|t| \geq t_{\alpha /2}(n-2)$ - $\alpha$에 관한 추론은
    특수한 상황이 아니고는 하지 않음. (절편의 값이0이 되는 것의 의미,
    설명변수가 0일 때의 종속변수의 값은 관심 X)

-   회귀모형을 이용한 예측(prediction) - 추정된 회귀식을 이용해 특정
    $x_0$ 값에 대응하는 반응변수 Y 의 값 추정 혹은 예측. - $E(Y_0)$ 의
    $x=x_0$ 일 때의 평균반응값이라 하면, $E(Y_0)$ 의 점추정 :
    $\hat{Y_0}  = \hat{\alpha} + \hat{\beta}x_0$ -
    $E(\hat{Y_0})  = E(\hat{\alpha} + \hat{\beta}x_0) = \alpha + \beta x_0$
    ,
    $Var(\hat{Y_0}) = Var(\hat{\alpha} + \hat{\beta}x_0 ) = Var(\bar{y} - \hat{\beta} (x_0 - \bar{x}) ) = Var(\bar{y}) + Var((x_0-\bar{x})\hat{\beta} ) + 2Cov(\bar{y}, (x_0-\bar{x}) \hat{\beta} )$
    $= \frac{\sigma^2}{n} + \frac{(x_0-\bar{x})^2 \sigma^2}{S_{xx}}$
    $\sigma$ 가 미지인 경우 $\hat{\sigma}$ 대입. -
    $\frac{(\hat{\alpha} + \hat{\beta}x_0)-(\alpha + \beta x_0)}{\hat{\sigma} \sqrt{n^{-1} + (x_0-\bar{x})^2/S_{xx}}} \sim t(n-2)$ -
    $\alpha + \beta x_0$ 에 대한 $100 ( 1-\alpha ) \%$ 신뢰구간 :
    $(\hat{\alpha} + \hat{\beta}x_0) \pm t_{\alpha/2} (n-2) {\hat{\sigma} \sqrt{n^{-1} + (x_0-\bar{x})^2/S_{xx}}}$ -
    검정통계량
    $T = \frac{(\hat{\alpha}+ \hat{\beta} x_0)-(\alpha + \beta x_0)}{\hat{\sigma} \sqrt{n^{-1} + (x_0-\bar{x})^2/S_{xx}}}$
    의 관측값을 t라고 하면, - 오른쪽 단측 검정의 경우, 유의확률
    $P = P(T \geq t) ,  T \sim t(n-2)$ 유의수준 $\alpha$ 의 기각역은
    $t\geq t_\alpha(n-2)$ - 왼쪽 단측 검정의 경우, 유의확률
    $P = P(T\leq t), T \sim t(n-2)$ 유의수준 $\alpha$ 의 기각역은
    $t\leq - t_\alpha(n-2)$ - 양측검정의 경우, 유의확률
    $P= P(|T| \geq |t|), T \sim t(n-2)$ 유의수준 $\alpha$의 기각역은
    $|t| \geq t_{\alpha /2}(n-2)$ - 평균반응의 신뢰구간에
    $(x_0-\bar{x})^2$ 의 항이 들어 있으므로, 신뢰구간의 너비는
    $x_0 = \bar{x}$ 일 때 가장 짧고 멀어질 수록 폭이 커짐. - 따라서
    설명변수의 값이 원자료의 범위를 많이 이탈하면 그 예측에는 신뢰성이
    떨어짐을 의미.

-   모형의 진단(diagnostic) 및 처방 (remedy) - 회귀 식의 유효성이 아닌
    해당 상황에서의 회귀모형 적용 자체의 타당성에 대한 검토
    $\rightarrow$ 먼저 산점도(scatter plot)을 그려서 알아봐야 함.
    (직관적 판단 필요) - 회귀 진단 항목 :
    $Y_i = \alpha + \beta x_i + \epsilon_i (i=1, 2, \cdots, n)$ 에서

    1.  $E(\epsilon_i) = 0$, i.e, $E(Y_i|x_i) = \alpha + \beta x_i$
        (선형성)

    2.  $Var(\epsilon_i) = \sigma^2 >0$ (등분산성)

    3.  $\epsilon_1 , \cdots, \epsilon_n$ 은 서로 독립 ( 독립성)

    4.  $\epsilon_i \sim N(0, \sigma^2)$ (정규성)

    5.  이상치(outlier) 나 영향력이 큰 관찰치 (influential
        observation)의 존재

-   산점도를 이용한 선형성 진단 - 산점도에서 두 변수가 비선형 관계를
    보이면, 변수변환 기법을 사용하거나 2차 이상의 다항식 또는 로그 함수
    등의 비선형 모형 사용 - 두 개의 직선이 동시에 나타나는 경우 : 두
    개의 그룹으로 나누어 각각 선형 모형을 시도 - 이상치(outlier)가
    보이는 경우 단순 오기에 의한 실수인지 점검, 그렇지 않다면 이상치를
    포함할지 혹은 제거 후 선형모형 시도할지 결정 - 영향력이 큰 관찰치가
    보이면 입력 실수인지 확인하고 영향력 판단 위해 관측값 제거 후 모형
    추정하여 추정치값, $R^2$ 의 값의 차 비교

-   잔차 분석(analysis of residual) - 잔차 : $e_i = y_i = \hat{y_i}$
    이며, 오차는 $\epsilon_i \sim_{i.i.d} N(0, \sigma^2)$ 에서 잔차는
    오차항의 관찰값으로 사용될 수 있음. - 회귀모형의 가정을 표준화된
    오차항으로 나타내자.
    $\frac{\epsilon_i - 0}{sd(\epsilon_i)} = \frac{Y_i - (\alpha + \beta x_i)}{\sigma} \sim_{i.i.d} N(0, 1)$
    $(i = 1, \cdots, n)$ - 이 때 잔차 $e_i$를 표준편차의 추정값으로
    나누어 얻는 (반) 스튜던트화 잔차(semi-studentized residual) :
    $\hat{e}_{st, i} = \frac{e_i}{\widehat{sd}(e_i)} = \frac{(y_i - \hat{y_i})}{\widehat{sd}(Y_i - \hat{Y_i})}$
    $(i = 1, \cdots, n)$ - 이 반 스튜던트화 잔차가 표준정규분포에서 서로
    독립인 n개의 관측값과 유사하게 나타나는지를 검토하여
    단순선형회귀모형의 적용 타당성 검증. - 잔차도 :
    $(x_i, \hat{e}_{st, i})$ 를 좌표평면에 나타내어 분석

    1.  대략 0에 대해 대칭적으로 나타나고(선형성)

    2.  설명변수의 값에 따른 잔차의 산포가 크게 다르지 않고(독립성)

    3.  점들이 특정 형식을 가지고 나타남이 없으며(등분산성)

    4.  표준 정규분포에서 $P(|Z|<2) \sim 0.95$ 이므로 모든 점이 $\pm 2$
        범위 내에 나타나는지 (정규성)

    -   통계적 추론의 순서

        1.  산점도를 그려 대략적 직선관계의 파악

        2.  최소제곱회귀직선, 평균제곱 오차 구하여 잔차분석 행햐고,
            스튜던트화 잔차도에 의한 통계모형의 적용의 유의성을
            검정한다.

        3.  잔차분석 통과시 신뢰구간이나 검정 같은 추론 행함.

## 다중회귀분석

-   두 개 이상의 설명변수와 반응변수의 변화를 선형 관계식으로 설명하는
    회귀 모형
    $Y_i = \beta_0 + \beta_1 x_{1i} + \beta_2 x_{2i} + \cdots + \beta_k x_{ki} + \epsilon_i$

-   다중선형 회귀식
    $E(Y_i ) = \beta_0 + \beta_1 x_{1i} + \beta_2 x_{2i} + \cdots + \beta_k x_{ki} + \epsilon_i$

-   다중선형회귀모형의 가정사항 : 단순선형회귀모형과 동일,
    $Y_i \sim_{i.i.d} N(\beta_0 + \sum_{j=1}^k \beta_j x_{ji}, \sigma^2)$
    ($\sigma^2$ unknown)

-   최소제곱법(Least squares method) : 다중선형회귀모형에서 오차의
    제곱합을 최소로 하는 최소제곱추정값으로 한다.

-   추정계수 $\hat{\beta}_j$의 해석 : j번째 설명변수 $x_j$를 제외한
    나머지가 고정되어있다는 가정 하에 $x_j$가 1 단위 변화할 때 y의
    변화량

-   $\hat{\beta}_0$는 Y절편으로 큰 의미 두지 않지만, 회귀식의 적합성
    높이기 위해 모형에 포함.

-   제곱합의 분해 (Decomposition) : SST = SSE + SSR -
    $\sum_{i=1}^n (y_i-\bar{y})^2 = \sum_{i=1}^n  (y_i-\hat{y_i})^2 + \sum_{i=1}^n (\hat{y_i}-\bar{y_i})^2$
    이며 각각 자유도 df= n-1, n-k-1, k -
    $MSE = \frac{SSE}{n-k-1} , MSR = \frac{SSR}{k}$

-   잔차(residual) :
    $e_i= y_i - \hat{y_i} = y_i-(\hat{\beta_0} +\sum_{i=1}^n \hat{\beta_j}x_{ji} )$
    이고 오차분산의 추정값 또한
    $\hat{\sigma}^2 = MSE = \frac{SSE}{n-k-1}= \frac{1}{n-k-1} \sum_{i=1}^n e_i^2$

-   결정계수
    $R^2 = \frac{SSR}{SST} = 1- \frac{SSE}{SST} = \frac{\sum_{i=1}^n (\hat{y_i} - \bar{y_i})^2}{\sum_{i=1}^n(y_i-\bar{y_i})^2}$

-   단순선형회귀모형에 대한 유의성 F 검정 - 귀무가설
    $H_0 : \beta_1 = \beta_2=\cdots =\beta_k = 0$ while 대립가설 $H_1 :$
    At least one $\beta_j \neq$ 0 - 검정통계량
    $F = \frac{SSR/k}{SSE / (n-k-1)} \sim F(k, n-k-1)$ (by Cochran's
    Theorem) - 유의확률 $P = P\{F\geq f\},  F \sim F(k, n-k-1)$ 이고,
    유의수준 $\alpha$ 의 기각역은 $f\geq F_\alpha (k, n-k-1)$ 인 오른쪽
    단측검정.

-   개별 계수 $\beta _j$ 에 대한 유의성 t 검정 - $\beta$에 대한
    $100(1-\alpha) \%$ 신뢰구간 :
    $\hat{\beta_j} \pm t_{\alpha/2}(n-k-1) s(\hat{\beta_j})$ -
    $H_0 : \beta_j = 0$ 이며, $H_1 : \beta_j \neq 0$ -귀무가설 하에서
    검정통계량
    $T = \frac{\hat{\beta_j}-0}{s(\hat{\beta_j})} \sim t(n-k-1)$ -
    양측검정의 경우이므로, 유의확률 $P= P(|T| \geq |t|), T \sim t(n-2)$
    유의수준 $\alpha$의 기각역은 $|t| \geq t_{\alpha /2}(n-k-1)$

-   다중선형회귀분석시 주의점 : 설명변수들 끼리 높은 상관계수를 갖게
    되면 그들 중 일부 변수가 비유의적으로 되는 경우가 상당히 많음.

-   회귀진단 ( regression diagnostics ) :

    1.  모형의 선형성(linearity)

    2.  오차의 등분산성(homoscedasticity), 독립성(independence)

    3.  이상값(outlier)의 존재

    4.  영향력이 큰 관찰치(influential observation) 의 존재

    5.  다중공선성(multicollinearity)

```{=html}
<!-- -->
```
-   다중공선성 : 설명변수중 하나와 다른 설명변수들의 선형결합이 매우
    높은 상관관계일 때 -\> 설명변수들 간의 선형독립성이 성립하지 않는
    경우.

    1.  개별 설명변수 끼리의 산점도에서 거의 직선에 가까운 선형관계를
        보이는 경우

    2.  설명변수 하나의 가감에 따라 다른 설명변수의 기울기 추정값의
        변동이 심한 경우

    3.  분산분석표에서 유의적으로 기울기가 0이 아니지만, 문제가 되는
        설명변수의 기울기는 유의적이지 않은 경우

    4.  유의성 F 검정에서는 유의하나 개별 t 검정에서는 유의하지 않은
        경우

    5.  분산확대인수를 계산

-   잔차분석 (analysis of residual) : 잔차도를 그려야 함. -
    $\hat{e}_{st, i} = \frac{e_i}{\widehat{sd}(e_i)} = \frac{(y_i - \hat{y_i})}{\widehat{sd}(Y_i - \hat{Y_i})}$ -
    다중회귀에서는 설명변수가 여러 개, x가 아닌 $y_i$를 x 축으로 하여
    그래프를 그림.

# 분산 분석

-   용어 : 종속변수, 반응 변수, 관측값 : Y \| 요인 - 실험에서 결과에
    영향 미칠 것으로 고려되는 변수. \| 처리 : 관찰되는 요인의 구체적 값
    or 범주 - 요인에 따라 처리한 정도에 따라 관측값이 어떻게
    달라지는지를 알아보는 것.

-   분산분석 (Analysis of Variance : ANOVA) : 특성값의 분산 or 변동을
    분석하여 3개 이상의 모집단 별 평균의 차이 판단하는 것. - 일원배치법
    (one-way ANOVA) , 확률화블록설계(randomized complete block design),
    이원배치법(two-way ANOVA)

## 일원배치법

-   특성값에 대한 한 종류의 인자의 영향을 조사하고자 할 때 사용.

-   완전랜덤화계획 : 실험이 랜덤 순서에 의해 시행, 관측한 반응변수의
    차이가 우연적 결과 or 처리효과에 의한 것인지 판단할 수 있어야 함 /
    반복 실시 : 우연에 좌우되지 않도록, 처리효과 보다 명확하게 볼 수
    있게 함. / 일원배치법의 통계적 모형 : k개의 모집단 각각에서 서로
    독립인 확률표본 추출

-   일원배치법 : 1개의 요인에 대해 2개 이상의 처리. (k개의 수준) , 각
    수준에서 $n_i$ 번의 반복 실험. (i=1 k) -기호 정리 : $y_{ij}$ : i번째
    처리의 jth index / $y_{i\cdot}$ : i번째 처리의 관측값의 합 /
    $\bar{y_{i \cdot}}$ : ith 처리 관측값의 평균 / $y_{\cdot \cdot}$ :
    모든 관측값의 합 / $\bar{y}_{\cdot \cdot}$ : 모든 관측값들의 평균

-   일원배치법의 모형 : $Y_{ij} = \mu_i + \epsilon_i$ 혹은,
    $Y_{ij}= \mu_i + \alpha_i + \epsilon_{ij}$ 이며, $\mu_i$는 ith
    처리효과의 평균, 기댓값. $\mu$는 처리효과 전체의 모평균. $\alpha_i$
    : ith 처리효과 = $\mu_i - \mu$ , $\epsilon_{ij}$ : 실험 오차 -
    귀무가설 $H_0 : \mu_1 = \mu_2 = \cdots = \mu_k$ $(or$
    $\alpha_1 = \alpha_2=\cdots=\alpha_k =0)$ 대립가설 $H_1 :$ Not all
    $\mu_i$ are equal (at least one $\alpha_i \neq 0)$

-   오차항 $\epsilon_{ij}$ 의 가정사항 :
    $\epsilon_{ij}\sim_{i.i.d} N(0, \sigma^2) \rightarrow Y_{ij} \sim_{i.i.d} N(\mu+\alpha_i, \sigma^2)$

    1.  $E(\epsilon_{ij}) = 0$ : 평균이 0

    2.  $Var(\epsilon_{ij}) = \sigma^2 > 0$ : 등분산성

    3.  $\epsilon_{11},\cdots,  \epsilon_{kn}$ 가 독립 : 독립성

    4.  $\epsilon_{ij} \sim N(0,  \sigma^2)$ : 정규성

-   일원배치법의 추정값들 - $\mu_i$ 의 추정값 : $\bar{y_{i\cdot}}$ /
    $\mu$의 추정값 : $\bar{y}_{\cdot \cdot}$ / $\alpha_i$ 의 추정값 :
    $\bar{y}_{i \cdot }- \bar{y}_{\cdot \cdot}$ / $y_{ij}$ 의 추정값 :
    $\bar{y}_{i \cdot}$ -
    $y_{ij} = \mu_i + \epsilon_i = E(y_{ij}) + \epsilon_{ij}$ (ideal
    model) vs
    $y_{ij} = \hat{y}_{ij} + e_{ij} = \hat{y}_{i \cdot} + e_{ij}$ (based
    on data estimates)

-   분산의 역할 : 분산이 너무 커도 귀무가설을 기각하기 힘들며, 분산이
    너무 작아도 또한 귀무가설 기각하기 쉬워진다.

-   제곱합의 분해 : SST = SSTR + SSE -
    $\sum_{i=1}^k \sum_{j=1}^n (y_{ij}- \bar{y}_{\cdot \cdot})^2 = n\sum_{i=1} ^k (\bar{y}_{i\cdot}- \bar{y}_{\cdot \cdot})^2 + \sum_{i=1}^k \sum_{j=1}^n(y_{ij} - \bar{y}_{i\cdot})^2$ -
    SSTR = $n\sum_{i=1}^k (\bar{y}_{i \cdot} - \bar{y}_{\cdot \cdot})^2$
    / SSE =
    $\sum_{i=1}^k \sum_{j=1}^n(y_{ij} - \bar{y}_{i\cdot})^2 = \sum_{j=1} ^{k} (n_j-1) s_j^2$
    ($s_i^2$ : ith treatment의 표본분산) - SST의 자유도 :
    $df  = N-1 \rightarrow$ N(nk) observed value - 1 constraint
    $\sum (y_{ij} - \bar{y}_{\cdot \cdot })  =0$ - SSTR의 자유도 :
    $df= k-1 \rightarrow$ k observed value - 1 constraint
    $\sum( \bar{y}_{i \cdot} - \bar{y}_{\cdot \cdot }) = 0$ - SSE의
    자유도 : $df = N-k \rightarrow$ (n observed value - 1 constraint
    $\bar{y}_{i \cdot}$ $\times$ k treatments = N-k

-   평균제곱과 간편 계산공식 : 제곱합 / df = 평균제곱, - SST =
    $\sum_{i=1}^k \sum_{j=1}^n(y_{ij})^2 - \frac{y_{\cdot \cdot}^2}{N}$ -
    SSTR =
    $n \sum_{i=1}^k (\bar{y}_{i\cdot})^2 - \frac{y_{\cdot \cdot}^2}{N}$

-   처리 효과의 유의성 검정 - 처리 효과의 유의성 검정에 대한 귀무가설
    $H_0 : \mu_1 = \mu_2 = \cdots = \mu_k$ or (
    $\alpha_1 = \alpha_2 = \cdots = \alpha_k = 0$ ) , $H_1 :$ not all
    $\mu_i$ are equal - 검정통계량
    $F = \frac{SSTR/k-1}{SSE / (N-k)} \sim F(k-1, N-k)$ (by Cochran's
    Theorem) - 유의확률 $P = P\{F\geq f\},  F \sim F(k-1, N-k)$ 이고,
    유의수준 $\alpha$ 의 기각역은 $f\geq F_\alpha (k-1, N-k)$ 인 오른쪽
    단측검정.

## 일원배치법 (반복수가 다른 경우)

-   1개의 요인(factor), k개의 처리(treatment), 각 수준에서 $n_i$ 번의
    반복 실험 -기호 정리 : $y_{ij}$ : i번째 처리의 jth index /
    $y_{i\cdot}$ : i번째 처리의 관측값의 합 / $\bar{y_{i \cdot}}$ : ith
    처리 관측값의 평균 / $y_{\cdot \cdot}$ : 모든 관측값의 합 /
    $\bar{y}_{\cdot \cdot}$ : 모든 관측값들의 평균

-   일원배치법의 모형 : $Y_{ij} = \mu_i + \epsilon_i$ 혹은,
    $Y_{ij}= \mu_i + \alpha_i + \epsilon_{ij}$ 이며, $\mu_i$는 ith
    처리효과의 평균, 기댓값. $\mu$는 처리효과 전체의 모평균. $\alpha_i$
    : ith 처리효과 = $\mu_i - \mu$ , $\epsilon_{ij}$ : 실험 오차 -
    귀무가설 $H_0 : \mu_1 = \mu_2 = \cdots = \mu_k$ $(or$
    $\alpha_1 = \alpha_2=\cdots=\alpha_k =0)$ 대립가설 $H_1 :$ Not all
    $\mu_i$ are equal (at least one $\alpha_i \neq 0)$

-   제곱합의 분해 : SST = SSTR + SSE -
    $\sum_{i=1}^k \sum_{j=1}^n (y_{ij}- \bar{y}_{\cdot \cdot})^2 = \sum_{i=1} ^k n_i(\bar{y}_{i\cdot}- \bar{y}_{\cdot \cdot})^2 + \sum_{i=1}^k \sum_{j=1}^n(y_{ij} - \bar{y}_{i\cdot})^2$ -
    SSTR =
    $\sum_{i=1}^k n_i(\bar{y}_{i \cdot} - \bar{y}_{\cdot \cdot})^2$ /
    SSE =
    $\sum_{i=1}^k \sum_{j=1}^n(y_{ij} - \bar{y}_{i\cdot})^2 = \sum_{j=1} ^{k} (n_j-1) s_j^2$
    ($s_i^2$ : ith treatment의 표본분산) - SST의 자유도 :
    $df  = N-1 \rightarrow$ N(nk) observed value - 1 constraint
    $\sum (y_{ij} - \bar{y}_{\cdot \cdot })  =0$ - SSTR의 자유도 :
    $df= k-1 \rightarrow$ k observed value - 1 constraint
    $\sum( \bar{y}_{i \cdot} - \bar{y}_{\cdot \cdot }) = 0$ - SSE의
    자유도 : $df = N-k \rightarrow$ (n observed value - 1 constraint
    $\bar{y}_{i \cdot}$ $\times$ k treatments = N-k

-   평균제곱과 간편 계산공식 : 제곱합 / df = 평균제곱, - SST =
    $\sum_{i=1}^k \sum_{j=1}^n(y_{ij})^2 - \frac{y_{\cdot \cdot}^2}{N}$ -
    SSTR =
    $\sum_{i=1}^k n_i(\bar{y}_{i\cdot})^2 - \frac{y_{\cdot \cdot}^2}{N}$

-   처리 효과의 유의성 검정 - 처리 효과의 유의성 검정에 대한 귀무가설
    $H_0 : \mu_1 = \mu_2 = \cdots = \mu_k$ or (
    $\alpha_1 = \alpha_2 = \cdots = \alpha_k = 0$ ) , $H_1 :$ not all
    $\mu_i$ are equal - 검정통계량
    $F = \frac{SSTR/k-1}{SSE / (N-k)} \sim F(k-1, N-k)$ (by Cochran's
    Theorem) - 유의확률 $P = P\{F\geq f\},  F \sim F(k-1, N-k)$ 이고,
    유의수준 $\alpha$ 의 기각역은 $f\geq F_\alpha (k-1, N-k)$ 인 오른쪽
    단측검정.

## 다중비교

-   일원배치법의 분석 결과 귀무가설이 기각되면, 그 차이를 보이는
    모집단이 어떤 것인지 추가적으로 분석해야 함. (Bonferroni의 방법)

-   가정사항 : 독립표본, 모집단 정규선, 모집단 등분산성

-   귀무가설 $H_0 : \mu_i = \mu_j$ , 대립가설 $H_1 : \mu_i \neq \mu_j$
    (for all $i\neq j$ , i=1 k, j=1 k)

-   다중비교에서 type 1 error 범할 확률 =
    $1- (1-\alpha)^{nC_2} \geq \alpha$

-   Bonferroni 수행절차

    1.  먼저 $C = nC_2$ 값을 구함.

    2.  $\alpha_E$ (familywise type 1 error) 가 주어지면 이를 C로 나누어
        $\alpha_*$ (elementwise type 1 error)를 구한다.

    3.  등분산 이표본 검정에서 사용한 $S_p^2$ 을 MSE로 대체하여 사용.

    4.  Rejection rule :
        $|\bar{y}_{i\cdot} - \bar{y}_{j\cdot} | > t_{\alpha_* /2 }(N-k) \sqrt{MSE(\frac{1}{n_i}+ \frac{1}{n_j})}$

## 확률화블록설계

-   블록 : 연구의 대상이 되는 개체들이 같거나 비슷한 특성 갖는 그룹을
    의미, 실험 진행 전 사전에 정의 되어야 함.

-   확률화블록설계 : 대응비교의 확장, 3개 이상의 모집단을 비교. 개체의
    이질성 식별가능한 경우 무작위가 아닌 단위를 비교적 균질한 그룹의
    블록으로 그룹화하여 그룹 내에서 랜덤하게 처리 할당. /
    외생변수(exogenous variable) 을 고려하여 외부요인에 의한 변동 제어.

-   RCBD : SST = SSTR + SSB + SSE (일원배치법의 SSE가 SSB + SSE로 나뉘어
    잔차의 제곱합이 줄어드는 효과.) -기호 정리 : $y_{ij}$ : i번째 처리의
    jth 블록의 관측값 / $y_{i\cdot}$ : i번째 처리의 관측값의 합 /
    $\bar{y_{i \cdot}}$ : ith 처리 관측값의 평균 / $y_{\cdot j}$ : j번째
    블록의 관측값의 합 / $\bar{y_{\cdot j}}$ : j번째 블록 관측값의 평균
    / $y_{\cdot \cdot}$ : 모든 관측값의 합 / $\bar{y}_{\cdot \cdot}$ :
    모든 관측값들의 평균

-   RCBD의 모형 : $Y_{ij} = \mu + \alpha_{i} + \beta_j + \epsilon_{ij}$
    이며, $\mu$는 처리효과 전체의 모평균, $\alpha_i , \beta_j$는 각각
    ith 처리효과, jth block효과의 평균.
    $\sum \alpha_i = \sum \beta_j = 0$ $\epsilon_{ij}$ 는 실험 오차에
    해당되는 확률변수

-   오차항 $\epsilon_{ij}$의 가정사항 :
    $\epsilon_{ij} \sim_{i.i.d} N(0, \sigma^2) \rightarrow Y_{ij} \sim_{i.i.d} N(\mu + \alpha_i + \beta_j , \sigma^2)$
    , 랜덤/독립분포, 정규분포, 등분산 가정.

-   모수들의 추정값 : $\hat{\mu} = \bar{y}_{\cdot \cdot}$ /
    $\hat{\alpha}_i = \bar{y}_{i \cdot} - \bar{y}_{\cdot \cdot}$ /
    $\hat{\beta}_i = \bar{y}_{\cdot i} - \bar{y}_{\cdot \cdot}$ /
    $\hat{y}_{ij} = \bar{y}_{i \cdot} + \bar{y}_{\cdot i} - \bar{y}_{\cdot \cdot}$

-   RCBD의 가설 : - 처리효과의 유의성 검정 : 귀무가설
    $H_0 : \alpha_1 = \alpha_2 = \cdots = \alpha_k = 0 \rightarrow$
    처리효과의 평균차는 없다. - Block 효과의 유의성 검정 : 귀무가설
    $H_0 : \beta_1 = \beta_2 = \cdots = \beta_b = 0 \rightarrow$ Block
    의 효과가 없다. (Block 효과는 외생변수의 영향 어느정도 제어 위해서
    만든 것이므로, 일반적으론 하지 않음.)

-   제곱합의 분해 : -
    $(y_{ij} - \bar{y}_{\cdot \cdot} ) = (\bar{y} _ {i \cdot} - \bar{y}_{\cdot \cdot}) + (\bar{y} _ {\cdot j} - \bar{y}_{\cdot \cdot} ) + (\bar{y}_{ij} - \bar{y}_{i \cdot} - \bar{y} _{\cdot j} + \bar{y} _ {\cdot \cdot})$
    : 전체 편차 = ith 처리효과에 대한 편차 + jth block효과에 의한 편차 +
    잔차 - SST =
    $\sum \sum (y_{ij} - \bar{y}_{\cdot \cdot }) ^2  = \sum_{i=1} ^k \sum_{j=1} ^b y_{ij}^2 - \frac{y_{\cdot \cdot}^2}{N}$
    (df = N-1) - SSTR =
    $b\sum_{i=1}^k(\bar{y}_{i\cdot} -\bar{y}_{\cdot \cdot}) ^2  = b\sum_{i=1} ^k \bar{y}_{i \cdot} ^2  - \frac{y_{\cdot \cdot }^2 }{N}$
    (df = k-1) - SSB =
    $k\sum_{j=1}^b(\bar{y}_{\cdot j} -\bar{y}_{\cdot \cdot}) ^2  = k\sum_{j=1} ^b \bar{y}_{\cdot j } ^2  - \frac{y_{\cdot \cdot }^2 }{N}$
    (df = b-1) - SSE = SST-SSTR-SSB (df = (k-1) (b-1) )

-   처리효과의 유의성검정 - 검정통계량
    $F = \frac{MSTR}{MSE} \sim F(k-1, (k-1)(b-1))$ - 귀무가설
    $H_0 : \alpha_1 = \alpha_2 = \cdots = \alpha_k = 0$ - 유의확률
    $P = P\{F \geq f_1\}$ $F \sim F(k-1, (k-1)(b-1))$ - 유의수준
    $\alpha$의 기각역 $f_1 \geq F_\alpha (k-1, (k-1)(b-1) )$

-   Block효과의 유의성검정 - 검정통계량
    $F = \frac{MSB}{MSE} \sim F(b-1, (k-1)(b-1))$ - 귀무가설
    $H_0 : \beta_1 = \beta_2 = \cdots = \beta_b = 0$ - 유의확률
    $P = P\{F \geq f_2\}$ $F \sim F(b-1, (k-1)(b-1))$ - 유의수준
    $\alpha$의 기각역 $f_2 \geq F_\alpha (b-1, (k-1)(b-1) )$

## 이원배치법

-   특성값 영향 주는 2개의 인자에 대해 조사, 요인 A에 a개의 처리그룹,
    B에 b개의 처리그룹. ab의 처리조합마다 n번씩 반복실험.

-   조건 : $a \times b \times n$ 의 전체 실험이 랜덤순서에 의해 시행,
    확률적으로 할당되어 독립성 보장 필요. 반복 실시 필요(2회 이상),
    분산이 같은 정규분포 따르는 독립표본임을 가정.

-   교호작용(interaction) : 반복 있는 이원배치법 -\> 한 요인의 평균에
    미치는 영향이 다른 요인의 처리그룹에 따라 달라지는 경우. 즉 두
    요인간 상호작용 있는 경우

-   그래프 (x축 : Factor A, y축 : 반응 평균, 그래프의 갯수를 Factor B의
    갯수만큼 그려 표현) - 두 그래프가 특정 모양으로 특정 비율로 그려짐 :
    서로 독립적으로 차이 보임. - 두 그래프가 특정 모양으로 포개어짐 :
    Factor A에 의한 차이는 유의, Factor B에 의한 차이는 유의하지 않음. -
    두 그래프가 직선으로 특정 비율로 그려짐 : Factor B에 의한 차이는
    유의, Factor A에 의한 차이는 유의하지 않음. - 서로 상관관계가 있음 :
    교호작용의 존재 (상호작용 있음)

-   기호 정리 : - $y_{ijk}$ : 요인 A의 ith 처리, 요인 B의 jth 처리에서
    k번째 index - $y_{i\cdot}$ : 요인 A의 i번째 처리그룹 내 모든
    관측값의 총합 - $\bar{y}_{i \cdot }$ : 요인 A의 i번째 처리그룹 내
    관측값의 평균 - $y_{\cdot j }$ : 요인 B의 j번째 처리그룹 내 모든
    관측값의 총합 - $\bar{y}_{\cdot j}$ : 요인 B의 j번째 처리그룹 내
    관측값의 평균 - $y_{ij\cdot}$ : 요인 A의 ith, 요인 B의 jth의 n개
    관측값들의 합 - $\bar{y}_{ij\cdot}$ : 요인 A의 ith, 요인 B의 jth의
    n개 관측값들의 평균 - $y_{\cdot \cdot \cdot}$ : 모든 관측값들의 합 -
    $\bar{y}_{\cdot \cdot \cdot}$ : 모든 관측값들의 평균

-   이원배치법의 모형 :
    $Y_{ijk} = \mu + \alpha_i + \beta_j + \gamma_{ij} + \epsilon_{ijk}$
    ($\gamma_{ij}$: i, j의 교호작용의 효과, 모든 교호작용을 i와
    j방향으로 더하면 0)

-   오차항의 가정사항 :
    $\epsilon_{ijk} \sim_{i.i.d} N(0, \sigma^2) \rightarrow N(\mu+\alpha_i +\beta_j + \gamma_{ij}, \sigma^2)$
    이며 독립성, 정규성, 등분산성 만족.

-   모수의 추정값 : $\hat{\mu} = \bar{y}_{\cdot \cdot \cdot}$ /
    $\hat{\alpha}_i = \bar{y}_{i \cdot \cdot} - \bar{y}_{\cdot \cdot \cdot}$
    /
    $\hat{\beta}_j = \bar{y}_{\cdot j \cdot}- \bar{y}_{\cdot \cdot \cdot}$
    /
    $\hat{\gamma}_{ij} = \bar{y}_{ij\cdot} - \bar{y}_{i\cdot\cdot} - \bar{y}_{\cdot j \cdot} + \bar{y} _{\cdot \cdot \cdot}$

-   제곱합의 분해 : SST = SSA + SSB + SSAB + SSE - SST
    =$\sum_{i=1} ^a \sum_{j=1}^b\sum_{k=1}^n (y_{ijk} - \bar{y}_{\cdot \cdot \cdot })^2= \sum_{i=1}^a \sum_{j=1}^b \sum_{k=1}^n y_{ijk}^2 - \frac{y_{\cdot \cdot \cdot}^2}{abn}$
    (총제곱합 df = abn-1) - SSA =
    $bn \sum_{i=1}^a (\bar{y}_{i \cdot \cdot}-\bar{y} _{\cdot \cdot \cdot} )^2 = \frac{1}{bn} \sum_{i=1} ^a y_{i\cdot\cdot}^2 - \frac{y_{\cdot \cdot \cdot}^2}{abn}$
    (요인 A의 제곱합 df = a-1) - SSB =
    $an \sum_{j=1}^b (\bar{y}_{\cdot j \cdot}-\bar{y} _{\cdot \cdot \cdot} )^2 =\frac{1}{an} \sum_{j=1} ^b y_{\cdot j\cdot}^2 - \frac{y_{\cdot \cdot \cdot}^2}{abn}$
    (요인 B의 제곱합 df = b-1) - SSAB =
    $n \sum_{i=1}^a \sum_{j=1} ^ b (y_{ijk} - \bar{y}_{ij\cdot} )^2 =  \frac{1}{n} \sum_{i=1} ^a \sum_{j=1}^b y_{ij\cdot}^2 - \frac{y_{\cdot \cdot \cdot}^2}{abn}-SSA-SSB$
    (교호작용의 제곱합 df = (a-1)(b-1)) - SSE =
    $\sum_{i=1}^a \sum_{j=1}^b \sum_{k=1}^n (y_{ijk}- \bar{y}_{ij\cdot})^2 = SST - SSAB - SSA - SSB$
    (잔차제곱합 df = ab(n-1))
