"use strict";
(self.webpackChunkflynt = self.webpackChunkflynt || []).push([[747], {
    1747: (e,t,n)=>{
        n.r(t),
        n(6265);
        var o = n(5311)
          , i = n.n(o);
        n(4043);
        var s = !1;
        if ("undefined" != typeof window) {
            var r = {
                get passive() {
                    s = !0
                }
            };
            window.addEventListener("testPassive", null, r),
            window.removeEventListener("testPassive", null, r)
        }
        var l = "undefined" != typeof window && window.navigator && window.navigator.platform && (/iP(ad|hone|od)/.test(window.navigator.platform) || "MacIntel" === window.navigator.platform && window.navigator.maxTouchPoints > 1)
          , a = []
          , u = !1
          , d = -1
          , c = void 0
          , h = void 0
          , v = function(e) {
            return a.some((function(t) {
                return !(!t.options.allowTouchMove || !t.options.allowTouchMove(e))
            }
            ))
        }
          , m = function(e) {
            var t = e || window.event;
            return !!v(t.target) || t.touches.length > 1 || (t.preventDefault && t.preventDefault(),
            !1)
        };
        class g extends window.HTMLElement {
            constructor(...e) {
                const t = super(...e);
                return t.init(),
                t
            }
            init() {
                this.$ = i()(this),
                this.bindFunctions(),
                this.bindEvents(),
                this.resolveElements()
            }
            bindFunctions() {
                this.triggerMenu = this.triggerMenu.bind(this)
            }
            bindEvents() {
                this.$.on("click", "[data-toggle-menu]", this.triggerMenu)
            }
            resolveElements() {
                this.$menu = i()(".menu", this),
                this.$menuButton = i()(".hamburger", this),
                this.$menuScroll = i()(".menu-scroll", this)
            }
            connectedCallback() {}
            triggerMenu(e) {
                var t;
                this.$.toggleClass("flyntComponent-menuIsOpen"),
                this.$menuButton.attr("aria-expanded", "false" === this.$menuButton.attr("aria-expanded") ? "true" : "false"),
                this.$.hasClass("flyntComponent-menuIsOpen") ? function(e, t) {
                    if (e) {
                        if (!a.some((function(t) {
                            return t.targetElement === e
                        }
                        ))) {
                            var n = {
                                targetElement: e,
                                options: t || {}
                            };
                            a = [].concat(function(e) {
                                if (Array.isArray(e)) {
                                    for (var t = 0, n = Array(e.length); t < e.length; t++)
                                        n[t] = e[t];
                                    return n
                                }
                                return Array.from(e)
                            }(a), [n]),
                            l ? (e.ontouchstart = function(e) {
                                1 === e.targetTouches.length && (d = e.targetTouches[0].clientY)
                            }
                            ,
                            e.ontouchmove = function(t) {
                                1 === t.targetTouches.length && function(e, t) {
                                    var n = e.targetTouches[0].clientY - d;
                                    !v(e.target) && (t && 0 === t.scrollTop && n > 0 || function(e) {
                                        return !!e && e.scrollHeight - e.scrollTop <= e.clientHeight
                                    }(t) && n < 0 ? m(e) : e.stopPropagation())
                                }(t, e)
                            }
                            ,
                            u || (document.addEventListener("touchmove", m, s ? {
                                passive: !1
                            } : void 0),
                            u = !0)) : function(e) {
                                if (void 0 === h) {
                                    var t = !!e && !0 === e.reserveScrollBarGap
                                      , n = window.innerWidth - document.documentElement.clientWidth;
                                    t && n > 0 && (h = document.body.style.paddingRight,
                                    document.body.style.paddingRight = n + "px")
                                }
                                void 0 === c && (c = document.body.style.overflow,
                                document.body.style.overflow = "hidden")
                            }(t)
                        }
                    } else
                        console.error("disableBodyScroll unsuccessful - targetElement must be provided when calling disableBodyScroll on IOS devices.")
                }(this.$menuScroll.get(0)) : ((t = this.$menuScroll.get(0)) ? (a = a.filter((function(e) {
                    return e.targetElement !== t
                }
                )),
                l ? (t.ontouchstart = null,
                t.ontouchmove = null,
                u && 0 === a.length && (document.removeEventListener("touchmove", m, s ? {
                    passive: !1
                } : void 0),
                u = !1)) : a.length || (void 0 !== h && (document.body.style.paddingRight = h,
                h = void 0),
                void 0 !== c && (document.body.style.overflow = c,
                c = void 0))) : console.error("enableBodyScroll unsuccessful - targetElement must be provided when calling enableBodyScroll on IOS devices."),
                this.$.addClass("flyntComponent-menuIsClosing"),
                setTimeout((()=>{
                    this.$.removeClass("flyntComponent-menuIsClosing")
                }
                ), 300))
            }
        }
        window.customElements.define("flynt-navigation-burger", g, {
            extends: "nav"
        })
    }
}]);
