"use strict";
(self.webpackChunkflynt = self.webpackChunkflynt || []).push([[167], {
    5652: (t,e,o)=>{
        o.r(e),
        o(6265);
        var i = o(5311)
          , s = o.n(i)
          , n = o(2632)
          , l = o.n(n)
          , a = o(1248)
          , r = o.n(a);
        class h extends window.HTMLDivElement {
            constructor(...t) {
                const e = super(...t);
                return e.init(),
                e
            }
            init() {
                this.$ = s()(this),
                this.resolveElements()
            }
            resolveElements() {
                this.$lottieBox = s()("[data-lottie-path]", this)
            }
            connectedCallback() {
                if (this.$lottieBox.length) {
                    const t = r().loadAnimation({
                        container: this.$lottieBox.get(0),
                        renderer: "svg",
                        loop: Boolean(this.$lottieBox.data("lottie-loop")),
                        autoplay: !1,
                        path: this.$lottieBox.data("lottie-path")
                    });
                    t.setSpeed(this.$lottieBox.data("lottie-speed")),
                    s()(window).on("resize", l()((()=>{
                        t.resize()
                    }
                    ), 200));
                    const e = new IntersectionObserver((o=>{
                        o.forEach((o=>{
                            !0 === Boolean(this.$lottieBox.data("lottie-loop")) ? o.intersectionRatio > 0 ? t.play() : t.stop() : o.intersectionRatio > 0 && (t.play(),
                            e.unobserve(this.$lottieBox.get(0)))
                        }
                        ))
                    }
                    ));
                    e.observe(this.$lottieBox.get(0))
                }
            }
        }
        window.customElements.define("flynt-hero-cta", h, {
            extends: "div"
        })
    }
}]);
