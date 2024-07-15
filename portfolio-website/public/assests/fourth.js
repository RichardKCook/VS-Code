"use strict";
(self.webpackChunkflynt = self.webpackChunkflynt || []).push([[411], {
    411: (e,t,s)=>{
        s.r(t),
        s(6265);
        var i = s(3682);
        class r extends window.HTMLDivElement {
            constructor(...e) {
                const t = super(...e);
                return t.init(),
                t
            }
            init() {
                this.props = this.getInitialProps(),
                this.resolveElements()
            }
            getInitialProps() {
                let e = {};
                try {
                    e = JSON.parse(this.querySelector('script[type="application/json"]').innerHTML)
                } catch (e) {}
                return e
            }
            resolveElements() {
                this.$firstSlider = this.querySelector("[data-first-slider]"),
                this.$secondSlider = this.querySelector("[data-second-slider]")
            }
            connectedCallback() {
                this.initSlider()
            }
            initSlider() {
                const {options: e} = this.props
                  , t = {
                    modules: [i.Qr, i.VS, i.pt, i.oM],
                    speed: 500,
                    grabCursor: !0,
                    loop: !0,
                    roundLengths: !0,
                    lazy: {
                        loadPrevNext: !0,
                        loadPrevNextAmount: 3
                    }
                };
                e.autoplay && e.autoplaySpeed && (t.autoplay = {
                    delay: e.autoplaySpeed
                }),
                this.firstSlider = new i.ZP(this.$firstSlider,t),
                delete t.autoplay,
                this.secondSlider = new i.ZP(this.$secondSlider,t),
                this.firstSlider.controller.control = this.secondSlider,
                this.secondSlider.controller.control = this.firstSlider
            }
        }
        window.customElements.define("flynt-block-gallery", r, {
            extends: "div"
        })
    }
}]);
