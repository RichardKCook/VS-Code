"use strict";
(self.webpackChunkflynt = self.webpackChunkflynt || []).push([[682], {
    8494: (e,t,s)=>{
        var i = s(3691)
          , a = TypeError;
        e.exports = function(e, t) {
            if (!delete e[t])
                throw new a("Cannot delete property " + i(t) + " of " + i(e))
        }
    }
    ,
    7365: (e,t,s)=>{
        var i = s(71).match(/firefox\/(\d+)/i);
        e.exports = !!i && +i[1]
    }
    ,
    7298: (e,t,s)=>{
        var i = s(71);
        e.exports = /MSIE|Trident/.test(i)
    }
    ,
    7922: (e,t,s)=>{
        var i = s(71).match(/AppleWebKit\/(\d+)\./);
        e.exports = !!i && +i[1]
    }
    ,
    5137: (e,t,s)=>{
        var i = s(9989)
          , a = s(8844)
          , n = s(509)
          , r = s(690)
          , l = s(6310)
          , o = s(8494)
          , d = s(4327)
          , p = s(3689)
          , c = s(382)
          , u = s(6834)
          , h = s(7365)
          , f = s(7298)
          , m = s(3615)
          , g = s(7922)
          , v = []
          , w = a(v.sort)
          , b = a(v.push)
          , C = p((function() {
            v.sort(void 0)
        }
        ))
          , y = p((function() {
            v.sort(null)
        }
        ))
          , x = u("sort")
          , T = !p((function() {
            if (m)
                return m < 70;
            if (!(h && h > 3)) {
                if (f)
                    return !0;
                if (g)
                    return g < 603;
                var e, t, s, i, a = "";
                for (e = 65; e < 76; e++) {
                    switch (t = String.fromCharCode(e),
                    e) {
                    case 66:
                    case 69:
                    case 70:
                    case 72:
                        s = 3;
                        break;
                    case 68:
                    case 71:
                        s = 4;
                        break;
                    default:
                        s = 2
                    }
                    for (i = 0; i < 47; i++)
                        v.push({
                            k: t + i,
                            v: s
                        })
                }
                for (v.sort((function(e, t) {
                    return t.v - e.v
                }
                )),
                i = 0; i < v.length; i++)
                    t = v[i].k.charAt(0),
                    a.charAt(a.length - 1) !== t && (a += t);
                return "DGBEFHACIJK" !== a
            }
        }
        ));
        i({
            target: "Array",
            proto: !0,
            forced: C || !y || !x || !T
        }, {
            sort: function(e) {
                void 0 !== e && n(e);
                var t = r(this);
                if (T)
                    return void 0 === e ? w(t) : w(t, e);
                var s, i, a = [], p = l(t);
                for (i = 0; i < p; i++)
                    i in t && b(a, t[i]);
                for (c(a, function(e) {
                    return function(t, s) {
                        return void 0 === s ? -1 : void 0 === t ? 1 : void 0 !== e ? +e(t, s) || 0 : d(t) > d(s) ? 1 : -1
                    }
                }(e)),
                s = l(a),
                i = 0; i < s; )
                    t[i] = a[i++];
                for (; i < p; )
                    o(t, i++);
                return t
            }
        })
    }
    ,
    3682: (e,t,s)=>{
        function i(e) {
            return null !== e && "object" == typeof e && "constructor"in e && e.constructor === Object
        }
        function a(e={}, t={}) {
            Object.keys(t).forEach((s=>{
                void 0 === e[s] ? e[s] = t[s] : i(t[s]) && i(e[s]) && Object.keys(t[s]).length > 0 && a(e[s], t[s])
            }
            ))
        }
        s.d(t, {
            s5: ()=>ne,
            pt: ()=>re,
            Qr: ()=>ae,
            oM: ()=>ie,
            W_: ()=>Z,
            tl: ()=>te,
            VS: ()=>se,
            ZP: ()=>J
        }),
        s(6265),
        s(8436);
        const n = {
            body: {},
            addEventListener() {},
            removeEventListener() {},
            activeElement: {
                blur() {},
                nodeName: ""
            },
            querySelector: ()=>null,
            querySelectorAll: ()=>[],
            getElementById: ()=>null,
            createEvent: ()=>({
                initEvent() {}
            }),
            createElement: ()=>({
                children: [],
                childNodes: [],
                style: {},
                setAttribute() {},
                getElementsByTagName: ()=>[]
            }),
            createElementNS: ()=>({}),
            importNode: ()=>null,
            location: {
                hash: "",
                host: "",
                hostname: "",
                href: "",
                origin: "",
                pathname: "",
                protocol: "",
                search: ""
            }
        };
        function r() {
            const e = "undefined" != typeof document ? document : {};
            return a(e, n),
            e
        }
        const l = {
            document: n,
            navigator: {
                userAgent: ""
            },
            location: {
                hash: "",
                host: "",
                hostname: "",
                href: "",
                origin: "",
                pathname: "",
                protocol: "",
                search: ""
            },
            history: {
                replaceState() {},
                pushState() {},
                go() {},
                back() {}
            },
            CustomEvent: function() {
                return this
            },
            addEventListener() {},
            removeEventListener() {},
            getComputedStyle: ()=>({
                getPropertyValue: ()=>""
            }),
            Image() {},
            Date() {},
            screen: {},
            setTimeout() {},
            clearTimeout() {},
            matchMedia: ()=>({}),
            requestAnimationFrame: e=>"undefined" == typeof setTimeout ? (e(),
            null) : setTimeout(e, 0),
            cancelAnimationFrame(e) {
                "undefined" != typeof setTimeout && clearTimeout(e)
            }
        };
        function o() {
            const e = "undefined" != typeof window ? window : {};
            return a(e, l),
            e
        }
        s(4043),
        s(7267);
        class d extends Array {
            constructor(e) {
                "number" == typeof e ? super(e) : (super(...e || []),
                function(e) {
                    const t = e.__proto__;
                    Object.defineProperty(e, "__proto__", {
                        get: ()=>t,
                        set(e) {
                            t.__proto__ = e
                        }
                    })
                }(this))
            }
        }
        function p(e=[]) {
            const t = [];
            return e.forEach((e=>{
                Array.isArray(e) ? t.push(...p(e)) : t.push(e)
            }
            )),
            t
        }
        function c(e, t) {
            return Array.prototype.filter.call(e, t)
        }
        function u(e, t) {
            const s = o()
              , i = r();
            let a = [];
            if (!t && e instanceof d)
                return e;
            if (!e)
                return new d(a);
            if ("string" == typeof e) {
                const s = e.trim();
                if (s.indexOf("<") >= 0 && s.indexOf(">") >= 0) {
                    let e = "div";
                    0 === s.indexOf("<li") && (e = "ul"),
                    0 === s.indexOf("<tr") && (e = "tbody"),
                    0 !== s.indexOf("<td") && 0 !== s.indexOf("<th") || (e = "tr"),
                    0 === s.indexOf("<tbody") && (e = "table"),
                    0 === s.indexOf("<option") && (e = "select");
                    const t = i.createElement(e);
                    t.innerHTML = s;
                    for (let e = 0; e < t.childNodes.length; e += 1)
                        a.push(t.childNodes[e])
                } else
                    a = function(e, t) {
                        if ("string" != typeof e)
                            return [e];
                        const s = []
                          , i = t.querySelectorAll(e);
                        for (let e = 0; e < i.length; e += 1)
                            s.push(i[e]);
                        return s
                    }(e.trim(), t || i)
            } else if (e.nodeType || e === s || e === i)
                a.push(e);
            else if (Array.isArray(e)) {
                if (e instanceof d)
                    return e;
                a = e
            }
            return new d(function(e) {
                const t = [];
                for (let s = 0; s < e.length; s += 1)
                    -1 === t.indexOf(e[s]) && t.push(e[s]);
                return t
            }(a))
        }
        u.fn = d.prototype;
        const h = "resize scroll".split(" ");
        function f(e) {
            return function(...t) {
                if (void 0 === t[0]) {
                    for (let t = 0; t < this.length; t += 1)
                        h.indexOf(e) < 0 && (e in this[t] ? this[t][e]() : u(this[t]).trigger(e));
                    return this
                }
                return this.on(e, ...t)
            }
        }
        f("click"),
        f("blur"),
        f("focus"),
        f("focusin"),
        f("focusout"),
        f("keyup"),
        f("keydown"),
        f("keypress"),
        f("submit"),
        f("change"),
        f("mousedown"),
        f("mousemove"),
        f("mouseup"),
        f("mouseenter"),
        f("mouseleave"),
        f("mouseout"),
        f("mouseover"),
        f("touchstart"),
        f("touchend"),
        f("touchmove"),
        f("resize"),
        f("scroll");
        const m = {
            addClass: function(...e) {
                const t = p(e.map((e=>e.split(" "))));
                return this.forEach((e=>{
                    e.classList.add(...t)
                }
                )),
                this
            },
            removeClass: function(...e) {
                const t = p(e.map((e=>e.split(" "))));
                return this.forEach((e=>{
                    e.classList.remove(...t)
                }
                )),
                this
            },
            hasClass: function(...e) {
                const t = p(e.map((e=>e.split(" "))));
                return c(this, (e=>t.filter((t=>e.classList.contains(t))).length > 0)).length > 0
            },
            toggleClass: function(...e) {
                const t = p(e.map((e=>e.split(" "))));
                this.forEach((e=>{
                    t.forEach((t=>{
                        e.classList.toggle(t)
                    }
                    ))
                }
                ))
            },
            attr: function(e, t) {
                if (1 === arguments.length && "string" == typeof e)
                    return this[0] ? this[0].getAttribute(e) : void 0;
                for (let s = 0; s < this.length; s += 1)
                    if (2 === arguments.length)
                        this[s].setAttribute(e, t);
                    else
                        for (const t in e)
                            this[s][t] = e[t],
                            this[s].setAttribute(t, e[t]);
                return this
            },
            removeAttr: function(e) {
                for (let t = 0; t < this.length; t += 1)
                    this[t].removeAttribute(e);
                return this
            },
            transform: function(e) {
                for (let t = 0; t < this.length; t += 1)
                    this[t].style.transform = e;
                return this
            },
            transition: function(e) {
                for (let t = 0; t < this.length; t += 1)
                    this[t].style.transitionDuration = "string" != typeof e ? `${e}ms` : e;
                return this
            },
            on: function(...e) {
                let[t,s,i,a] = e;
                function n(e) {
                    const t = e.target;
                    if (!t)
                        return;
                    const a = e.target.dom7EventData || [];
                    if (a.indexOf(e) < 0 && a.unshift(e),
                    u(t).is(s))
                        i.apply(t, a);
                    else {
                        const e = u(t).parents();
                        for (let t = 0; t < e.length; t += 1)
                            u(e[t]).is(s) && i.apply(e[t], a)
                    }
                }
                function r(e) {
                    const t = e && e.target && e.target.dom7EventData || [];
                    t.indexOf(e) < 0 && t.unshift(e),
                    i.apply(this, t)
                }
                "function" == typeof e[1] && ([t,i,a] = e,
                s = void 0),
                a || (a = !1);
                const l = t.split(" ");
                let o;
                for (let e = 0; e < this.length; e += 1) {
                    const t = this[e];
                    if (s)
                        for (o = 0; o < l.length; o += 1) {
                            const e = l[o];
                            t.dom7LiveListeners || (t.dom7LiveListeners = {}),
                            t.dom7LiveListeners[e] || (t.dom7LiveListeners[e] = []),
                            t.dom7LiveListeners[e].push({
                                listener: i,
                                proxyListener: n
                            }),
                            t.addEventListener(e, n, a)
                        }
                    else
                        for (o = 0; o < l.length; o += 1) {
                            const e = l[o];
                            t.dom7Listeners || (t.dom7Listeners = {}),
                            t.dom7Listeners[e] || (t.dom7Listeners[e] = []),
                            t.dom7Listeners[e].push({
                                listener: i,
                                proxyListener: r
                            }),
                            t.addEventListener(e, r, a)
                        }
                }
                return this
            },
            off: function(...e) {
                let[t,s,i,a] = e;
                "function" == typeof e[1] && ([t,i,a] = e,
                s = void 0),
                a || (a = !1);
                const n = t.split(" ");
                for (let e = 0; e < n.length; e += 1) {
                    const t = n[e];
                    for (let e = 0; e < this.length; e += 1) {
                        const n = this[e];
                        let r;
                        if (!s && n.dom7Listeners ? r = n.dom7Listeners[t] : s && n.dom7LiveListeners && (r = n.dom7LiveListeners[t]),
                        r && r.length)
                            for (let e = r.length - 1; e >= 0; e -= 1) {
                                const s = r[e];
                                i && s.listener === i || i && s.listener && s.listener.dom7proxy && s.listener.dom7proxy === i ? (n.removeEventListener(t, s.proxyListener, a),
                                r.splice(e, 1)) : i || (n.removeEventListener(t, s.proxyListener, a),
                                r.splice(e, 1))
                            }
                    }
                }
                return this
            },
            trigger: function(...e) {
                const t = o()
                  , s = e[0].split(" ")
                  , i = e[1];
                for (let a = 0; a < s.length; a += 1) {
                    const n = s[a];
                    for (let s = 0; s < this.length; s += 1) {
                        const a = this[s];
                        if (t.CustomEvent) {
                            const s = new t.CustomEvent(n,{
                                detail: i,
                                bubbles: !0,
                                cancelable: !0
                            });
                            a.dom7EventData = e.filter(((e,t)=>t > 0)),
                            a.dispatchEvent(s),
                            a.dom7EventData = [],
                            delete a.dom7EventData
                        }
                    }
                }
                return this
            },
            transitionEnd: function(e) {
                const t = this;
                return e && t.on("transitionend", (function s(i) {
                    i.target === this && (e.call(this, i),
                    t.off("transitionend", s))
                }
                )),
                this
            },
            outerWidth: function(e) {
                if (this.length > 0) {
                    if (e) {
                        const e = this.styles();
                        return this[0].offsetWidth + parseFloat(e.getPropertyValue("margin-right")) + parseFloat(e.getPropertyValue("margin-left"))
                    }
                    return this[0].offsetWidth
                }
                return null
            },
            outerHeight: function(e) {
                if (this.length > 0) {
                    if (e) {
                        const e = this.styles();
                        return this[0].offsetHeight + parseFloat(e.getPropertyValue("margin-top")) + parseFloat(e.getPropertyValue("margin-bottom"))
                    }
                    return this[0].offsetHeight
                }
                return null
            },
            styles: function() {
                const e = o();
                return this[0] ? e.getComputedStyle(this[0], null) : {}
            },
            offset: function() {
                if (this.length > 0) {
                    const e = o()
                      , t = r()
                      , s = this[0]
                      , i = s.getBoundingClientRect()
                      , a = t.body
                      , n = s.clientTop || a.clientTop || 0
                      , l = s.clientLeft || a.clientLeft || 0
                      , d = s === e ? e.scrollY : s.scrollTop
                      , p = s === e ? e.scrollX : s.scrollLeft;
                    return {
                        top: i.top + d - n,
                        left: i.left + p - l
                    }
                }
                return null
            },
            css: function(e, t) {
                const s = o();
                let i;
                if (1 === arguments.length) {
                    if ("string" != typeof e) {
                        for (i = 0; i < this.length; i += 1)
                            for (const t in e)
                                this[i].style[t] = e[t];
                        return this
                    }
                    if (this[0])
                        return s.getComputedStyle(this[0], null).getPropertyValue(e)
                }
                if (2 === arguments.length && "string" == typeof e) {
                    for (i = 0; i < this.length; i += 1)
                        this[i].style[e] = t;
                    return this
                }
                return this
            },
            each: function(e) {
                return e ? (this.forEach(((t,s)=>{
                    e.apply(t, [t, s])
                }
                )),
                this) : this
            },
            html: function(e) {
                if (void 0 === e)
                    return this[0] ? this[0].innerHTML : null;
                for (let t = 0; t < this.length; t += 1)
                    this[t].innerHTML = e;
                return this
            },
            text: function(e) {
                if (void 0 === e)
                    return this[0] ? this[0].textContent.trim() : null;
                for (let t = 0; t < this.length; t += 1)
                    this[t].textContent = e;
                return this
            },
            is: function(e) {
                const t = o()
                  , s = r()
                  , i = this[0];
                let a, n;
                if (!i || void 0 === e)
                    return !1;
                if ("string" == typeof e) {
                    if (i.matches)
                        return i.matches(e);
                    if (i.webkitMatchesSelector)
                        return i.webkitMatchesSelector(e);
                    if (i.msMatchesSelector)
                        return i.msMatchesSelector(e);
                    for (a = u(e),
                    n = 0; n < a.length; n += 1)
                        if (a[n] === i)
                            return !0;
                    return !1
                }
                if (e === s)
                    return i === s;
                if (e === t)
                    return i === t;
                if (e.nodeType || e instanceof d) {
                    for (a = e.nodeType ? [e] : e,
                    n = 0; n < a.length; n += 1)
                        if (a[n] === i)
                            return !0;
                    return !1
                }
                return !1
            },
            index: function() {
                let e, t = this[0];
                if (t) {
                    for (e = 0; null !== (t = t.previousSibling); )
                        1 === t.nodeType && (e += 1);
                    return e
                }
            },
            eq: function(e) {
                if (void 0 === e)
                    return this;
                const t = this.length;
                if (e > t - 1)
                    return u([]);
                if (e < 0) {
                    const s = t + e;
                    return u(s < 0 ? [] : [this[s]])
                }
                return u([this[e]])
            },
            append: function(...e) {
                let t;
                const s = r();
                for (let i = 0; i < e.length; i += 1) {
                    t = e[i];
                    for (let e = 0; e < this.length; e += 1)
                        if ("string" == typeof t) {
                            const i = s.createElement("div");
                            for (i.innerHTML = t; i.firstChild; )
                                this[e].appendChild(i.firstChild)
                        } else if (t instanceof d)
                            for (let s = 0; s < t.length; s += 1)
                                this[e].appendChild(t[s]);
                        else
                            this[e].appendChild(t)
                }
                return this
            },
            prepend: function(e) {
                const t = r();
                let s, i;
                for (s = 0; s < this.length; s += 1)
                    if ("string" == typeof e) {
                        const a = t.createElement("div");
                        for (a.innerHTML = e,
                        i = a.childNodes.length - 1; i >= 0; i -= 1)
                            this[s].insertBefore(a.childNodes[i], this[s].childNodes[0])
                    } else if (e instanceof d)
                        for (i = 0; i < e.length; i += 1)
                            this[s].insertBefore(e[i], this[s].childNodes[0]);
                    else
                        this[s].insertBefore(e, this[s].childNodes[0]);
                return this
            },
            next: function(e) {
                return this.length > 0 ? e ? this[0].nextElementSibling && u(this[0].nextElementSibling).is(e) ? u([this[0].nextElementSibling]) : u([]) : this[0].nextElementSibling ? u([this[0].nextElementSibling]) : u([]) : u([])
            },
            nextAll: function(e) {
                const t = [];
                let s = this[0];
                if (!s)
                    return u([]);
                for (; s.nextElementSibling; ) {
                    const i = s.nextElementSibling;
                    e ? u(i).is(e) && t.push(i) : t.push(i),
                    s = i
                }
                return u(t)
            },
            prev: function(e) {
                if (this.length > 0) {
                    const t = this[0];
                    return e ? t.previousElementSibling && u(t.previousElementSibling).is(e) ? u([t.previousElementSibling]) : u([]) : t.previousElementSibling ? u([t.previousElementSibling]) : u([])
                }
                return u([])
            },
            prevAll: function(e) {
                const t = [];
                let s = this[0];
                if (!s)
                    return u([]);
                for (; s.previousElementSibling; ) {
                    const i = s.previousElementSibling;
                    e ? u(i).is(e) && t.push(i) : t.push(i),
                    s = i
                }
                return u(t)
            },
            parent: function(e) {
                const t = [];
                for (let s = 0; s < this.length; s += 1)
                    null !== this[s].parentNode && (e ? u(this[s].parentNode).is(e) && t.push(this[s].parentNode) : t.push(this[s].parentNode));
                return u(t)
            },
            parents: function(e) {
                const t = [];
                for (let s = 0; s < this.length; s += 1) {
                    let i = this[s].parentNode;
                    for (; i; )
                        e ? u(i).is(e) && t.push(i) : t.push(i),
                        i = i.parentNode
                }
                return u(t)
            },
            closest: function(e) {
                let t = this;
                return void 0 === e ? u([]) : (t.is(e) || (t = t.parents(e).eq(0)),
                t)
            },
            find: function(e) {
                const t = [];
                for (let s = 0; s < this.length; s += 1) {
                    const i = this[s].querySelectorAll(e);
                    for (let e = 0; e < i.length; e += 1)
                        t.push(i[e])
                }
                return u(t)
            },
            children: function(e) {
                const t = [];
                for (let s = 0; s < this.length; s += 1) {
                    const i = this[s].children;
                    for (let s = 0; s < i.length; s += 1)
                        e && !u(i[s]).is(e) || t.push(i[s])
                }
                return u(t)
            },
            filter: function(e) {
                return u(c(this, e))
            },
            remove: function() {
                for (let e = 0; e < this.length; e += 1)
                    this[e].parentNode && this[e].parentNode.removeChild(this[e]);
                return this
            }
        };
        Object.keys(m).forEach((e=>{
            Object.defineProperty(u.fn, e, {
                value: m[e],
                writable: !0
            })
        }
        ));
        var g = u;
        function v(e, t=0) {
            return setTimeout(e, t)
        }
        function w() {
            return Date.now()
        }
        function b(e) {
            return "object" == typeof e && null !== e && e.constructor && "Object" === Object.prototype.toString.call(e).slice(8, -1)
        }
        function C(...e) {
            const t = Object(e[0])
              , s = ["__proto__", "constructor", "prototype"];
            for (let a = 1; a < e.length; a += 1) {
                const n = e[a];
                if (null != n && (i = n,
                !("undefined" != typeof window && void 0 !== window.HTMLElement ? i instanceof HTMLElement : i && (1 === i.nodeType || 11 === i.nodeType)))) {
                    const e = Object.keys(Object(n)).filter((e=>s.indexOf(e) < 0));
                    for (let s = 0, i = e.length; s < i; s += 1) {
                        const i = e[s]
                          , a = Object.getOwnPropertyDescriptor(n, i);
                        void 0 !== a && a.enumerable && (b(t[i]) && b(n[i]) ? n[i].__swiper__ ? t[i] = n[i] : C(t[i], n[i]) : !b(t[i]) && b(n[i]) ? (t[i] = {},
                        n[i].__swiper__ ? t[i] = n[i] : C(t[i], n[i])) : t[i] = n[i])
                    }
                }
            }
            var i;
            return t
        }
        function y(e, t, s) {
            e.style.setProperty(t, s)
        }
        function x({swiper: e, targetPosition: t, side: s}) {
            const i = o()
              , a = -e.translate;
            let n, r = null;
            const l = e.params.speed;
            e.wrapperEl.style.scrollSnapType = "none",
            i.cancelAnimationFrame(e.cssModeFrameID);
            const d = t > a ? "next" : "prev"
              , p = (e,t)=>"next" === d && e >= t || "prev" === d && e <= t
              , c = ()=>{
                n = (new Date).getTime(),
                null === r && (r = n);
                const o = Math.max(Math.min((n - r) / l, 1), 0)
                  , d = .5 - Math.cos(o * Math.PI) / 2;
                let u = a + d * (t - a);
                if (p(u, t) && (u = t),
                e.wrapperEl.scrollTo({
                    [s]: u
                }),
                p(u, t))
                    return e.wrapperEl.style.overflow = "hidden",
                    e.wrapperEl.style.scrollSnapType = "",
                    setTimeout((()=>{
                        e.wrapperEl.style.overflow = "",
                        e.wrapperEl.scrollTo({
                            [s]: u
                        })
                    }
                    )),
                    void i.cancelAnimationFrame(e.cssModeFrameID);
                e.cssModeFrameID = i.requestAnimationFrame(c)
            }
            ;
            c()
        }
        let T, S, E;
        function $() {
            return T || (T = function() {
                const e = o()
                  , t = r();
                return {
                    smoothScroll: t.documentElement && "scrollBehavior"in t.documentElement.style,
                    touch: !!("ontouchstart"in e || e.DocumentTouch && t instanceof e.DocumentTouch),
                    passiveListener: function() {
                        let t = !1;
                        try {
                            const s = Object.defineProperty({}, "passive", {
                                get() {
                                    t = !0
                                }
                            });
                            e.addEventListener("testPassiveListener", null, s)
                        } catch (e) {}
                        return t
                    }(),
                    gestures: "ongesturestart"in e
                }
            }()),
            T
        }
        var M = {
            on(e, t, s) {
                const i = this;
                if ("function" != typeof t)
                    return i;
                const a = s ? "unshift" : "push";
                return e.split(" ").forEach((e=>{
                    i.eventsListeners[e] || (i.eventsListeners[e] = []),
                    i.eventsListeners[e][a](t)
                }
                )),
                i
            },
            once(e, t, s) {
                const i = this;
                if ("function" != typeof t)
                    return i;
                function a(...s) {
                    i.off(e, a),
                    a.__emitterProxy && delete a.__emitterProxy,
                    t.apply(i, s)
                }
                return a.__emitterProxy = t,
                i.on(e, a, s)
            },
            onAny(e, t) {
                const s = this;
                if ("function" != typeof e)
                    return s;
                const i = t ? "unshift" : "push";
                return s.eventsAnyListeners.indexOf(e) < 0 && s.eventsAnyListeners[i](e),
                s
            },
            offAny(e) {
                const t = this;
                if (!t.eventsAnyListeners)
                    return t;
                const s = t.eventsAnyListeners.indexOf(e);
                return s >= 0 && t.eventsAnyListeners.splice(s, 1),
                t
            },
            off(e, t) {
                const s = this;
                return s.eventsListeners ? (e.split(" ").forEach((e=>{
                    void 0 === t ? s.eventsListeners[e] = [] : s.eventsListeners[e] && s.eventsListeners[e].forEach(((i,a)=>{
                        (i === t || i.__emitterProxy && i.__emitterProxy === t) && s.eventsListeners[e].splice(a, 1)
                    }
                    ))
                }
                )),
                s) : s
            },
            emit(...e) {
                const t = this;
                if (!t.eventsListeners)
                    return t;
                let s, i, a;
                return "string" == typeof e[0] || Array.isArray(e[0]) ? (s = e[0],
                i = e.slice(1, e.length),
                a = t) : (s = e[0].events,
                i = e[0].data,
                a = e[0].context || t),
                i.unshift(a),
                (Array.isArray(s) ? s : s.split(" ")).forEach((e=>{
                    t.eventsAnyListeners && t.eventsAnyListeners.length && t.eventsAnyListeners.forEach((t=>{
                        t.apply(a, [e, ...i])
                    }
                    )),
                    t.eventsListeners && t.eventsListeners[e] && t.eventsListeners[e].forEach((e=>{
                        e.apply(a, i)
                    }
                    ))
                }
                )),
                t
            }
        }
          , k = {
            updateSize: function() {
                const e = this;
                let t, s;
                const i = e.$el;
                t = void 0 !== e.params.width && null !== e.params.width ? e.params.width : i[0].clientWidth,
                s = void 0 !== e.params.height && null !== e.params.height ? e.params.height : i[0].clientHeight,
                0 === t && e.isHorizontal() || 0 === s && e.isVertical() || (t = t - parseInt(i.css("padding-left") || 0, 10) - parseInt(i.css("padding-right") || 0, 10),
                s = s - parseInt(i.css("padding-top") || 0, 10) - parseInt(i.css("padding-bottom") || 0, 10),
                Number.isNaN(t) && (t = 0),
                Number.isNaN(s) && (s = 0),
                Object.assign(e, {
                    width: t,
                    height: s,
                    size: e.isHorizontal() ? t : s
                }))
            },
            updateSlides: function() {
                const e = this;
                function t(t) {
                    return e.isHorizontal() ? t : {
                        width: "height",
                        "margin-top": "margin-left",
                        "margin-bottom ": "margin-right",
                        "margin-left": "margin-top",
                        "margin-right": "margin-bottom",
                        "padding-left": "padding-top",
                        "padding-right": "padding-bottom",
                        marginRight: "marginBottom"
                    }[t]
                }
                function s(e, s) {
                    return parseFloat(e.getPropertyValue(t(s)) || 0)
                }
                const i = e.params
                  , {$wrapperEl: a, size: n, rtlTranslate: r, wrongRTL: l} = e
                  , o = e.virtual && i.virtual.enabled
                  , d = o ? e.virtual.slides.length : e.slides.length
                  , p = a.children(`.${e.params.slideClass}`)
                  , c = o ? e.virtual.slides.length : p.length;
                let u = [];
                const h = []
                  , f = [];
                let m = i.slidesOffsetBefore;
                "function" == typeof m && (m = i.slidesOffsetBefore.call(e));
                let g = i.slidesOffsetAfter;
                "function" == typeof g && (g = i.slidesOffsetAfter.call(e));
                const v = e.snapGrid.length
                  , w = e.slidesGrid.length;
                let b = i.spaceBetween
                  , C = -m
                  , x = 0
                  , T = 0;
                if (void 0 === n)
                    return;
                "string" == typeof b && b.indexOf("%") >= 0 && (b = parseFloat(b.replace("%", "")) / 100 * n),
                e.virtualSize = -b,
                r ? p.css({
                    marginLeft: "",
                    marginBottom: "",
                    marginTop: ""
                }) : p.css({
                    marginRight: "",
                    marginBottom: "",
                    marginTop: ""
                }),
                i.centeredSlides && i.cssMode && (y(e.wrapperEl, "--swiper-centered-offset-before", ""),
                y(e.wrapperEl, "--swiper-centered-offset-after", ""));
                const S = i.grid && i.grid.rows > 1 && e.grid;
                let E;
                S && e.grid.initSlides(c);
                const $ = "auto" === i.slidesPerView && i.breakpoints && Object.keys(i.breakpoints).filter((e=>void 0 !== i.breakpoints[e].slidesPerView)).length > 0;
                for (let a = 0; a < c; a += 1) {
                    E = 0;
                    const r = p.eq(a);
                    if (S && e.grid.updateSlide(a, r, c, t),
                    "none" !== r.css("display")) {
                        if ("auto" === i.slidesPerView) {
                            $ && (p[a].style[t("width")] = "");
                            const n = getComputedStyle(r[0])
                              , l = r[0].style.transform
                              , o = r[0].style.webkitTransform;
                            if (l && (r[0].style.transform = "none"),
                            o && (r[0].style.webkitTransform = "none"),
                            i.roundLengths)
                                E = e.isHorizontal() ? r.outerWidth(!0) : r.outerHeight(!0);
                            else {
                                const e = s(n, "width")
                                  , t = s(n, "padding-left")
                                  , i = s(n, "padding-right")
                                  , a = s(n, "margin-left")
                                  , l = s(n, "margin-right")
                                  , o = n.getPropertyValue("box-sizing");
                                if (o && "border-box" === o)
                                    E = e + a + l;
                                else {
                                    const {clientWidth: s, offsetWidth: n} = r[0];
                                    E = e + t + i + a + l + (n - s)
                                }
                            }
                            l && (r[0].style.transform = l),
                            o && (r[0].style.webkitTransform = o),
                            i.roundLengths && (E = Math.floor(E))
                        } else
                            E = (n - (i.slidesPerView - 1) * b) / i.slidesPerView,
                            i.roundLengths && (E = Math.floor(E)),
                            p[a] && (p[a].style[t("width")] = `${E}px`);
                        p[a] && (p[a].swiperSlideSize = E),
                        f.push(E),
                        i.centeredSlides ? (C = C + E / 2 + x / 2 + b,
                        0 === x && 0 !== a && (C = C - n / 2 - b),
                        0 === a && (C = C - n / 2 - b),
                        Math.abs(C) < .001 && (C = 0),
                        i.roundLengths && (C = Math.floor(C)),
                        T % i.slidesPerGroup == 0 && u.push(C),
                        h.push(C)) : (i.roundLengths && (C = Math.floor(C)),
                        (T - Math.min(e.params.slidesPerGroupSkip, T)) % e.params.slidesPerGroup == 0 && u.push(C),
                        h.push(C),
                        C = C + E + b),
                        e.virtualSize += E + b,
                        x = E,
                        T += 1
                    }
                }
                if (e.virtualSize = Math.max(e.virtualSize, n) + g,
                r && l && ("slide" === i.effect || "coverflow" === i.effect) && a.css({
                    width: `${e.virtualSize + i.spaceBetween}px`
                }),
                i.setWrapperSize && a.css({
                    [t("width")]: `${e.virtualSize + i.spaceBetween}px`
                }),
                S && e.grid.updateWrapperSize(E, u, t),
                !i.centeredSlides) {
                    const t = [];
                    for (let s = 0; s < u.length; s += 1) {
                        let a = u[s];
                        i.roundLengths && (a = Math.floor(a)),
                        u[s] <= e.virtualSize - n && t.push(a)
                    }
                    u = t,
                    Math.floor(e.virtualSize - n) - Math.floor(u[u.length - 1]) > 1 && u.push(e.virtualSize - n)
                }
                if (0 === u.length && (u = [0]),
                0 !== i.spaceBetween) {
                    const s = e.isHorizontal() && r ? "marginLeft" : t("marginRight");
                    p.filter(((e,t)=>!i.cssMode || t !== p.length - 1)).css({
                        [s]: `${b}px`
                    })
                }
                if (i.centeredSlides && i.centeredSlidesBounds) {
                    let e = 0;
                    f.forEach((t=>{
                        e += t + (i.spaceBetween ? i.spaceBetween : 0)
                    }
                    )),
                    e -= i.spaceBetween;
                    const t = e - n;
                    u = u.map((e=>e < 0 ? -m : e > t ? t + g : e))
                }
                if (i.centerInsufficientSlides) {
                    let e = 0;
                    if (f.forEach((t=>{
                        e += t + (i.spaceBetween ? i.spaceBetween : 0)
                    }
                    )),
                    e -= i.spaceBetween,
                    e < n) {
                        const t = (n - e) / 2;
                        u.forEach(((e,s)=>{
                            u[s] = e - t
                        }
                        )),
                        h.forEach(((e,s)=>{
                            h[s] = e + t
                        }
                        ))
                    }
                }
                if (Object.assign(e, {
                    slides: p,
                    snapGrid: u,
                    slidesGrid: h,
                    slidesSizesGrid: f
                }),
                i.centeredSlides && i.cssMode && !i.centeredSlidesBounds) {
                    y(e.wrapperEl, "--swiper-centered-offset-before", -u[0] + "px"),
                    y(e.wrapperEl, "--swiper-centered-offset-after", e.size / 2 - f[f.length - 1] / 2 + "px");
                    const t = -e.snapGrid[0]
                      , s = -e.slidesGrid[0];
                    e.snapGrid = e.snapGrid.map((e=>e + t)),
                    e.slidesGrid = e.slidesGrid.map((e=>e + s))
                }
                c !== d && e.emit("slidesLengthChange"),
                u.length !== v && (e.params.watchOverflow && e.checkOverflow(),
                e.emit("snapGridLengthChange")),
                h.length !== w && e.emit("slidesGridLengthChange"),
                i.watchSlidesProgress && e.updateSlidesOffset()
            },
            updateAutoHeight: function(e) {
                const t = this
                  , s = []
                  , i = t.virtual && t.params.virtual.enabled;
                let a, n = 0;
                "number" == typeof e ? t.setTransition(e) : !0 === e && t.setTransition(t.params.speed);
                const r = e=>i ? t.slides.filter((t=>parseInt(t.getAttribute("data-swiper-slide-index"), 10) === e))[0] : t.slides.eq(e)[0];
                if ("auto" !== t.params.slidesPerView && t.params.slidesPerView > 1)
                    if (t.params.centeredSlides)
                        t.visibleSlides.each((e=>{
                            s.push(e)
                        }
                        ));
                    else
                        for (a = 0; a < Math.ceil(t.params.slidesPerView); a += 1) {
                            const e = t.activeIndex + a;
                            if (e > t.slides.length && !i)
                                break;
                            s.push(r(e))
                        }
                else
                    s.push(r(t.activeIndex));
                for (a = 0; a < s.length; a += 1)
                    if (void 0 !== s[a]) {
                        const e = s[a].offsetHeight;
                        n = e > n ? e : n
                    }
                (n || 0 === n) && t.$wrapperEl.css("height", `${n}px`)
            },
            updateSlidesOffset: function() {
                const e = this
                  , t = e.slides;
                for (let s = 0; s < t.length; s += 1)
                    t[s].swiperSlideOffset = e.isHorizontal() ? t[s].offsetLeft : t[s].offsetTop
            },
            updateSlidesProgress: function(e=this && this.translate || 0) {
                const t = this
                  , s = t.params
                  , {slides: i, rtlTranslate: a, snapGrid: n} = t;
                if (0 === i.length)
                    return;
                void 0 === i[0].swiperSlideOffset && t.updateSlidesOffset();
                let r = -e;
                a && (r = e),
                i.removeClass(s.slideVisibleClass),
                t.visibleSlidesIndexes = [],
                t.visibleSlides = [];
                for (let e = 0; e < i.length; e += 1) {
                    const l = i[e];
                    let o = l.swiperSlideOffset;
                    s.cssMode && s.centeredSlides && (o -= i[0].swiperSlideOffset);
                    const d = (r + (s.centeredSlides ? t.minTranslate() : 0) - o) / (l.swiperSlideSize + s.spaceBetween)
                      , p = (r - n[0] + (s.centeredSlides ? t.minTranslate() : 0) - o) / (l.swiperSlideSize + s.spaceBetween)
                      , c = -(r - o)
                      , u = c + t.slidesSizesGrid[e];
                    (c >= 0 && c < t.size - 1 || u > 1 && u <= t.size || c <= 0 && u >= t.size) && (t.visibleSlides.push(l),
                    t.visibleSlidesIndexes.push(e),
                    i.eq(e).addClass(s.slideVisibleClass)),
                    l.progress = a ? -d : d,
                    l.originalProgress = a ? -p : p
                }
                t.visibleSlides = g(t.visibleSlides)
            },
            updateProgress: function(e) {
                const t = this;
                if (void 0 === e) {
                    const s = t.rtlTranslate ? -1 : 1;
                    e = t && t.translate && t.translate * s || 0
                }
                const s = t.params
                  , i = t.maxTranslate() - t.minTranslate();
                let {progress: a, isBeginning: n, isEnd: r} = t;
                const l = n
                  , o = r;
                0 === i ? (a = 0,
                n = !0,
                r = !0) : (a = (e - t.minTranslate()) / i,
                n = a <= 0,
                r = a >= 1),
                Object.assign(t, {
                    progress: a,
                    isBeginning: n,
                    isEnd: r
                }),
                (s.watchSlidesProgress || s.centeredSlides && s.autoHeight) && t.updateSlidesProgress(e),
                n && !l && t.emit("reachBeginning toEdge"),
                r && !o && t.emit("reachEnd toEdge"),
                (l && !n || o && !r) && t.emit("fromEdge"),
                t.emit("progress", a)
            },
            updateSlidesClasses: function() {
                const e = this
                  , {slides: t, params: s, $wrapperEl: i, activeIndex: a, realIndex: n} = e
                  , r = e.virtual && s.virtual.enabled;
                let l;
                t.removeClass(`${s.slideActiveClass} ${s.slideNextClass} ${s.slidePrevClass} ${s.slideDuplicateActiveClass} ${s.slideDuplicateNextClass} ${s.slideDuplicatePrevClass}`),
                l = r ? e.$wrapperEl.find(`.${s.slideClass}[data-swiper-slide-index="${a}"]`) : t.eq(a),
                l.addClass(s.slideActiveClass),
                s.loop && (l.hasClass(s.slideDuplicateClass) ? i.children(`.${s.slideClass}:not(.${s.slideDuplicateClass})[data-swiper-slide-index="${n}"]`).addClass(s.slideDuplicateActiveClass) : i.children(`.${s.slideClass}.${s.slideDuplicateClass}[data-swiper-slide-index="${n}"]`).addClass(s.slideDuplicateActiveClass));
                let o = l.nextAll(`.${s.slideClass}`).eq(0).addClass(s.slideNextClass);
                s.loop && 0 === o.length && (o = t.eq(0),
                o.addClass(s.slideNextClass));
                let d = l.prevAll(`.${s.slideClass}`).eq(0).addClass(s.slidePrevClass);
                s.loop && 0 === d.length && (d = t.eq(-1),
                d.addClass(s.slidePrevClass)),
                s.loop && (o.hasClass(s.slideDuplicateClass) ? i.children(`.${s.slideClass}:not(.${s.slideDuplicateClass})[data-swiper-slide-index="${o.attr("data-swiper-slide-index")}"]`).addClass(s.slideDuplicateNextClass) : i.children(`.${s.slideClass}.${s.slideDuplicateClass}[data-swiper-slide-index="${o.attr("data-swiper-slide-index")}"]`).addClass(s.slideDuplicateNextClass),
                d.hasClass(s.slideDuplicateClass) ? i.children(`.${s.slideClass}:not(.${s.slideDuplicateClass})[data-swiper-slide-index="${d.attr("data-swiper-slide-index")}"]`).addClass(s.slideDuplicatePrevClass) : i.children(`.${s.slideClass}.${s.slideDuplicateClass}[data-swiper-slide-index="${d.attr("data-swiper-slide-index")}"]`).addClass(s.slideDuplicatePrevClass)),
                e.emitSlidesClasses()
            },
            updateActiveIndex: function(e) {
                const t = this
                  , s = t.rtlTranslate ? t.translate : -t.translate
                  , {slidesGrid: i, snapGrid: a, params: n, activeIndex: r, realIndex: l, snapIndex: o} = t;
                let d, p = e;
                if (void 0 === p) {
                    for (let e = 0; e < i.length; e += 1)
                        void 0 !== i[e + 1] ? s >= i[e] && s < i[e + 1] - (i[e + 1] - i[e]) / 2 ? p = e : s >= i[e] && s < i[e + 1] && (p = e + 1) : s >= i[e] && (p = e);
                    n.normalizeSlideIndex && (p < 0 || void 0 === p) && (p = 0)
                }
                if (a.indexOf(s) >= 0)
                    d = a.indexOf(s);
                else {
                    const e = Math.min(n.slidesPerGroupSkip, p);
                    d = e + Math.floor((p - e) / n.slidesPerGroup)
                }
                if (d >= a.length && (d = a.length - 1),
                p === r)
                    return void (d !== o && (t.snapIndex = d,
                    t.emit("snapIndexChange")));
                const c = parseInt(t.slides.eq(p).attr("data-swiper-slide-index") || p, 10);
                Object.assign(t, {
                    snapIndex: d,
                    realIndex: c,
                    previousIndex: r,
                    activeIndex: p
                }),
                t.emit("activeIndexChange"),
                t.emit("snapIndexChange"),
                l !== c && t.emit("realIndexChange"),
                (t.initialized || t.params.runCallbacksOnInit) && t.emit("slideChange")
            },
            updateClickedSlide: function(e) {
                const t = this
                  , s = t.params
                  , i = g(e).closest(`.${s.slideClass}`)[0];
                let a, n = !1;
                if (i)
                    for (let e = 0; e < t.slides.length; e += 1)
                        if (t.slides[e] === i) {
                            n = !0,
                            a = e;
                            break
                        }
                if (!i || !n)
                    return t.clickedSlide = void 0,
                    void (t.clickedIndex = void 0);
                t.clickedSlide = i,
                t.virtual && t.params.virtual.enabled ? t.clickedIndex = parseInt(g(i).attr("data-swiper-slide-index"), 10) : t.clickedIndex = a,
                s.slideToClickedSlide && void 0 !== t.clickedIndex && t.clickedIndex !== t.activeIndex && t.slideToClickedSlide()
            }
        }
          , P = {
            getTranslate: function(e=(this.isHorizontal() ? "x" : "y")) {
                const {params: t, rtlTranslate: s, translate: i, $wrapperEl: a} = this;
                if (t.virtualTranslate)
                    return s ? -i : i;
                if (t.cssMode)
                    return i;
                let n = function(e, t="x") {
                    const s = o();
                    let i, a, n;
                    const r = function(e) {
                        const t = o();
                        let s;
                        return t.getComputedStyle && (s = t.getComputedStyle(e, null)),
                        !s && e.currentStyle && (s = e.currentStyle),
                        s || (s = e.style),
                        s
                    }(e);
                    return s.WebKitCSSMatrix ? (a = r.transform || r.webkitTransform,
                    a.split(",").length > 6 && (a = a.split(", ").map((e=>e.replace(",", "."))).join(", ")),
                    n = new s.WebKitCSSMatrix("none" === a ? "" : a)) : (n = r.MozTransform || r.OTransform || r.MsTransform || r.msTransform || r.transform || r.getPropertyValue("transform").replace("translate(", "matrix(1, 0, 0, 1,"),
                    i = n.toString().split(",")),
                    "x" === t && (a = s.WebKitCSSMatrix ? n.m41 : 16 === i.length ? parseFloat(i[12]) : parseFloat(i[4])),
                    "y" === t && (a = s.WebKitCSSMatrix ? n.m42 : 16 === i.length ? parseFloat(i[13]) : parseFloat(i[5])),
                    a || 0
                }(a[0], e);
                return s && (n = -n),
                n || 0
            },
            setTranslate: function(e, t) {
                const s = this
                  , {rtlTranslate: i, params: a, $wrapperEl: n, wrapperEl: r, progress: l} = s;
                let o, d = 0, p = 0;
                s.isHorizontal() ? d = i ? -e : e : p = e,
                a.roundLengths && (d = Math.floor(d),
                p = Math.floor(p)),
                a.cssMode ? r[s.isHorizontal() ? "scrollLeft" : "scrollTop"] = s.isHorizontal() ? -d : -p : a.virtualTranslate || n.transform(`translate3d(${d}px, ${p}px, 0px)`),
                s.previousTranslate = s.translate,
                s.translate = s.isHorizontal() ? d : p;
                const c = s.maxTranslate() - s.minTranslate();
                o = 0 === c ? 0 : (e - s.minTranslate()) / c,
                o !== l && s.updateProgress(e),
                s.emit("setTranslate", s.translate, t)
            },
            minTranslate: function() {
                return -this.snapGrid[0]
            },
            maxTranslate: function() {
                return -this.snapGrid[this.snapGrid.length - 1]
            },
            translateTo: function(e=0, t=this.params.speed, s=!0, i=!0, a) {
                const n = this
                  , {params: r, wrapperEl: l} = n;
                if (n.animating && r.preventInteractionOnTransition)
                    return !1;
                const o = n.minTranslate()
                  , d = n.maxTranslate();
                let p;
                if (p = i && e > o ? o : i && e < d ? d : e,
                n.updateProgress(p),
                r.cssMode) {
                    const e = n.isHorizontal();
                    if (0 === t)
                        l[e ? "scrollLeft" : "scrollTop"] = -p;
                    else {
                        if (!n.support.smoothScroll)
                            return x({
                                swiper: n,
                                targetPosition: -p,
                                side: e ? "left" : "top"
                            }),
                            !0;
                        l.scrollTo({
                            [e ? "left" : "top"]: -p,
                            behavior: "smooth"
                        })
                    }
                    return !0
                }
                return 0 === t ? (n.setTransition(0),
                n.setTranslate(p),
                s && (n.emit("beforeTransitionStart", t, a),
                n.emit("transitionEnd"))) : (n.setTransition(t),
                n.setTranslate(p),
                s && (n.emit("beforeTransitionStart", t, a),
                n.emit("transitionStart")),
                n.animating || (n.animating = !0,
                n.onTranslateToWrapperTransitionEnd || (n.onTranslateToWrapperTransitionEnd = function(e) {
                    n && !n.destroyed && e.target === this && (n.$wrapperEl[0].removeEventListener("transitionend", n.onTranslateToWrapperTransitionEnd),
                    n.$wrapperEl[0].removeEventListener("webkitTransitionEnd", n.onTranslateToWrapperTransitionEnd),
                    n.onTranslateToWrapperTransitionEnd = null,
                    delete n.onTranslateToWrapperTransitionEnd,
                    s && n.emit("transitionEnd"))
                }
                ),
                n.$wrapperEl[0].addEventListener("transitionend", n.onTranslateToWrapperTransitionEnd),
                n.$wrapperEl[0].addEventListener("webkitTransitionEnd", n.onTranslateToWrapperTransitionEnd))),
                !0
            }
        };
        function L({swiper: e, runCallbacks: t, direction: s, step: i}) {
            const {activeIndex: a, previousIndex: n} = e;
            let r = s;
            if (r || (r = a > n ? "next" : a < n ? "prev" : "reset"),
            e.emit(`transition${i}`),
            t && a !== n) {
                if ("reset" === r)
                    return void e.emit(`slideResetTransition${i}`);
                e.emit(`slideChangeTransition${i}`),
                "next" === r ? e.emit(`slideNextTransition${i}`) : e.emit(`slidePrevTransition${i}`)
            }
        }
        var O = {
            setTransition: function(e, t) {
                const s = this;
                s.params.cssMode || s.$wrapperEl.transition(e),
                s.emit("setTransition", e, t)
            },
            transitionStart: function(e=!0, t) {
                const s = this
                  , {params: i} = s;
                i.cssMode || (i.autoHeight && s.updateAutoHeight(),
                L({
                    swiper: s,
                    runCallbacks: e,
                    direction: t,
                    step: "Start"
                }))
            },
            transitionEnd: function(e=!0, t) {
                const s = this
                  , {params: i} = s;
                s.animating = !1,
                i.cssMode || (s.setTransition(0),
                L({
                    swiper: s,
                    runCallbacks: e,
                    direction: t,
                    step: "End"
                }))
            }
        }
          , z = {
            slideTo: function(e=0, t=this.params.speed, s=!0, i, a) {
                if ("number" != typeof e && "string" != typeof e)
                    throw new Error(`The 'index' argument cannot have type other than 'number' or 'string'. [${typeof e}] given.`);
                if ("string" == typeof e) {
                    const t = parseInt(e, 10);
                    if (!isFinite(t))
                        throw new Error(`The passed-in 'index' (string) couldn't be converted to 'number'. [${e}] given.`);
                    e = t
                }
                const n = this;
                let r = e;
                r < 0 && (r = 0);
                const {params: l, snapGrid: o, slidesGrid: d, previousIndex: p, activeIndex: c, rtlTranslate: u, wrapperEl: h, enabled: f} = n;
                if (n.animating && l.preventInteractionOnTransition || !f && !i && !a)
                    return !1;
                const m = Math.min(n.params.slidesPerGroupSkip, r);
                let g = m + Math.floor((r - m) / n.params.slidesPerGroup);
                g >= o.length && (g = o.length - 1),
                (c || l.initialSlide || 0) === (p || 0) && s && n.emit("beforeSlideChangeStart");
                const v = -o[g];
                if (n.updateProgress(v),
                l.normalizeSlideIndex)
                    for (let e = 0; e < d.length; e += 1) {
                        const t = -Math.floor(100 * v)
                          , s = Math.floor(100 * d[e])
                          , i = Math.floor(100 * d[e + 1]);
                        void 0 !== d[e + 1] ? t >= s && t < i - (i - s) / 2 ? r = e : t >= s && t < i && (r = e + 1) : t >= s && (r = e)
                    }
                if (n.initialized && r !== c) {
                    if (!n.allowSlideNext && v < n.translate && v < n.minTranslate())
                        return !1;
                    if (!n.allowSlidePrev && v > n.translate && v > n.maxTranslate() && (c || 0) !== r)
                        return !1
                }
                let w;
                if (w = r > c ? "next" : r < c ? "prev" : "reset",
                u && -v === n.translate || !u && v === n.translate)
                    return n.updateActiveIndex(r),
                    l.autoHeight && n.updateAutoHeight(),
                    n.updateSlidesClasses(),
                    "slide" !== l.effect && n.setTranslate(v),
                    "reset" !== w && (n.transitionStart(s, w),
                    n.transitionEnd(s, w)),
                    !1;
                if (l.cssMode) {
                    const e = n.isHorizontal()
                      , s = u ? v : -v;
                    if (0 === t) {
                        const t = n.virtual && n.params.virtual.enabled;
                        t && (n.wrapperEl.style.scrollSnapType = "none",
                        n._immediateVirtual = !0),
                        h[e ? "scrollLeft" : "scrollTop"] = s,
                        t && requestAnimationFrame((()=>{
                            n.wrapperEl.style.scrollSnapType = "",
                            n._swiperImmediateVirtual = !1
                        }
                        ))
                    } else {
                        if (!n.support.smoothScroll)
                            return x({
                                swiper: n,
                                targetPosition: s,
                                side: e ? "left" : "top"
                            }),
                            !0;
                        h.scrollTo({
                            [e ? "left" : "top"]: s,
                            behavior: "smooth"
                        })
                    }
                    return !0
                }
                return n.setTransition(t),
                n.setTranslate(v),
                n.updateActiveIndex(r),
                n.updateSlidesClasses(),
                n.emit("beforeTransitionStart", t, i),
                n.transitionStart(s, w),
                0 === t ? n.transitionEnd(s, w) : n.animating || (n.animating = !0,
                n.onSlideToWrapperTransitionEnd || (n.onSlideToWrapperTransitionEnd = function(e) {
                    n && !n.destroyed && e.target === this && (n.$wrapperEl[0].removeEventListener("transitionend", n.onSlideToWrapperTransitionEnd),
                    n.$wrapperEl[0].removeEventListener("webkitTransitionEnd", n.onSlideToWrapperTransitionEnd),
                    n.onSlideToWrapperTransitionEnd = null,
                    delete n.onSlideToWrapperTransitionEnd,
                    n.transitionEnd(s, w))
                }
                ),
                n.$wrapperEl[0].addEventListener("transitionend", n.onSlideToWrapperTransitionEnd),
                n.$wrapperEl[0].addEventListener("webkitTransitionEnd", n.onSlideToWrapperTransitionEnd)),
                !0
            },
            slideToLoop: function(e=0, t=this.params.speed, s=!0, i) {
                const a = this;
                let n = e;
                return a.params.loop && (n += a.loopedSlides),
                a.slideTo(n, t, s, i)
            },
            slideNext: function(e=this.params.speed, t=!0, s) {
                const i = this
                  , {animating: a, enabled: n, params: r} = i;
                if (!n)
                    return i;
                let l = r.slidesPerGroup;
                "auto" === r.slidesPerView && 1 === r.slidesPerGroup && r.slidesPerGroupAuto && (l = Math.max(i.slidesPerViewDynamic("current", !0), 1));
                const o = i.activeIndex < r.slidesPerGroupSkip ? 1 : l;
                if (r.loop) {
                    if (a && r.loopPreventsSlide)
                        return !1;
                    i.loopFix(),
                    i._clientLeft = i.$wrapperEl[0].clientLeft
                }
                return r.rewind && i.isEnd ? i.slideTo(0, e, t, s) : i.slideTo(i.activeIndex + o, e, t, s)
            },
            slidePrev: function(e=this.params.speed, t=!0, s) {
                const i = this
                  , {params: a, animating: n, snapGrid: r, slidesGrid: l, rtlTranslate: o, enabled: d} = i;
                if (!d)
                    return i;
                if (a.loop) {
                    if (n && a.loopPreventsSlide)
                        return !1;
                    i.loopFix(),
                    i._clientLeft = i.$wrapperEl[0].clientLeft
                }
                function p(e) {
                    return e < 0 ? -Math.floor(Math.abs(e)) : Math.floor(e)
                }
                const c = p(o ? i.translate : -i.translate)
                  , u = r.map((e=>p(e)));
                let h = r[u.indexOf(c) - 1];
                if (void 0 === h && a.cssMode) {
                    let e;
                    r.forEach(((t,s)=>{
                        c >= t && (e = s)
                    }
                    )),
                    void 0 !== e && (h = r[e > 0 ? e - 1 : e])
                }
                let f = 0;
                return void 0 !== h && (f = l.indexOf(h),
                f < 0 && (f = i.activeIndex - 1),
                "auto" === a.slidesPerView && 1 === a.slidesPerGroup && a.slidesPerGroupAuto && (f = f - i.slidesPerViewDynamic("previous", !0) + 1,
                f = Math.max(f, 0))),
                a.rewind && i.isBeginning ? i.slideTo(i.slides.length - 1, e, t, s) : i.slideTo(f, e, t, s)
            },
            slideReset: function(e=this.params.speed, t=!0, s) {
                return this.slideTo(this.activeIndex, e, t, s)
            },
            slideToClosest: function(e=this.params.speed, t=!0, s, i=.5) {
                const a = this;
                let n = a.activeIndex;
                const r = Math.min(a.params.slidesPerGroupSkip, n)
                  , l = r + Math.floor((n - r) / a.params.slidesPerGroup)
                  , o = a.rtlTranslate ? a.translate : -a.translate;
                if (o >= a.snapGrid[l]) {
                    const e = a.snapGrid[l];
                    o - e > (a.snapGrid[l + 1] - e) * i && (n += a.params.slidesPerGroup)
                } else {
                    const e = a.snapGrid[l - 1];
                    o - e <= (a.snapGrid[l] - e) * i && (n -= a.params.slidesPerGroup)
                }
                return n = Math.max(n, 0),
                n = Math.min(n, a.slidesGrid.length - 1),
                a.slideTo(n, e, t, s)
            },
            slideToClickedSlide: function() {
                const e = this
                  , {params: t, $wrapperEl: s} = e
                  , i = "auto" === t.slidesPerView ? e.slidesPerViewDynamic() : t.slidesPerView;
                let a, n = e.clickedIndex;
                if (t.loop) {
                    if (e.animating)
                        return;
                    a = parseInt(g(e.clickedSlide).attr("data-swiper-slide-index"), 10),
                    t.centeredSlides ? n < e.loopedSlides - i / 2 || n > e.slides.length - e.loopedSlides + i / 2 ? (e.loopFix(),
                    n = s.children(`.${t.slideClass}[data-swiper-slide-index="${a}"]:not(.${t.slideDuplicateClass})`).eq(0).index(),
                    v((()=>{
                        e.slideTo(n)
                    }
                    ))) : e.slideTo(n) : n > e.slides.length - i ? (e.loopFix(),
                    n = s.children(`.${t.slideClass}[data-swiper-slide-index="${a}"]:not(.${t.slideDuplicateClass})`).eq(0).index(),
                    v((()=>{
                        e.slideTo(n)
                    }
                    ))) : e.slideTo(n)
                } else
                    e.slideTo(n)
            }
        }
          , I = {
            loopCreate: function() {
                const e = this
                  , t = r()
                  , {params: s, $wrapperEl: i} = e
                  , a = i.children().length > 0 ? g(i.children()[0].parentNode) : i;
                a.children(`.${s.slideClass}.${s.slideDuplicateClass}`).remove();
                let n = a.children(`.${s.slideClass}`);
                if (s.loopFillGroupWithBlank) {
                    const e = s.slidesPerGroup - n.length % s.slidesPerGroup;
                    if (e !== s.slidesPerGroup) {
                        for (let i = 0; i < e; i += 1) {
                            const e = g(t.createElement("div")).addClass(`${s.slideClass} ${s.slideBlankClass}`);
                            a.append(e)
                        }
                        n = a.children(`.${s.slideClass}`)
                    }
                }
                "auto" !== s.slidesPerView || s.loopedSlides || (s.loopedSlides = n.length),
                e.loopedSlides = Math.ceil(parseFloat(s.loopedSlides || s.slidesPerView, 10)),
                e.loopedSlides += s.loopAdditionalSlides,
                e.loopedSlides > n.length && (e.loopedSlides = n.length);
                const l = []
                  , o = [];
                n.each(((t,s)=>{
                    const i = g(t);
                    s < e.loopedSlides && o.push(t),
                    s < n.length && s >= n.length - e.loopedSlides && l.push(t),
                    i.attr("data-swiper-slide-index", s)
                }
                ));
                for (let e = 0; e < o.length; e += 1)
                    a.append(g(o[e].cloneNode(!0)).addClass(s.slideDuplicateClass));
                for (let e = l.length - 1; e >= 0; e -= 1)
                    a.prepend(g(l[e].cloneNode(!0)).addClass(s.slideDuplicateClass))
            },
            loopFix: function() {
                const e = this;
                e.emit("beforeLoopFix");
                const {activeIndex: t, slides: s, loopedSlides: i, allowSlidePrev: a, allowSlideNext: n, snapGrid: r, rtlTranslate: l} = e;
                let o;
                e.allowSlidePrev = !0,
                e.allowSlideNext = !0;
                const d = -r[t] - e.getTranslate();
                t < i ? (o = s.length - 3 * i + t,
                o += i,
                e.slideTo(o, 0, !1, !0) && 0 !== d && e.setTranslate((l ? -e.translate : e.translate) - d)) : t >= s.length - i && (o = -s.length + t + i,
                o += i,
                e.slideTo(o, 0, !1, !0) && 0 !== d && e.setTranslate((l ? -e.translate : e.translate) - d)),
                e.allowSlidePrev = a,
                e.allowSlideNext = n,
                e.emit("loopFix")
            },
            loopDestroy: function() {
                const {$wrapperEl: e, params: t, slides: s} = this;
                e.children(`.${t.slideClass}.${t.slideDuplicateClass},.${t.slideClass}.${t.slideBlankClass}`).remove(),
                s.removeAttr("data-swiper-slide-index")
            }
        };
        function A(e) {
            const t = this
              , s = r()
              , i = o()
              , a = t.touchEventsData
              , {params: n, touches: l, enabled: d} = t;
            if (!d)
                return;
            if (t.animating && n.preventInteractionOnTransition)
                return;
            !t.animating && n.cssMode && n.loop && t.loopFix();
            let p = e;
            p.originalEvent && (p = p.originalEvent);
            let c = g(p.target);
            if ("wrapper" === n.touchEventsTarget && !c.closest(t.wrapperEl).length)
                return;
            if (a.isTouchEvent = "touchstart" === p.type,
            !a.isTouchEvent && "which"in p && 3 === p.which)
                return;
            if (!a.isTouchEvent && "button"in p && p.button > 0)
                return;
            if (a.isTouched && a.isMoved)
                return;
            n.noSwipingClass && "" !== n.noSwipingClass && p.target && p.target.shadowRoot && e.path && e.path[0] && (c = g(e.path[0]));
            const u = n.noSwipingSelector ? n.noSwipingSelector : `.${n.noSwipingClass}`
              , h = !(!p.target || !p.target.shadowRoot);
            if (n.noSwiping && (h ? function(e, t=this) {
                return function t(s) {
                    return s && s !== r() && s !== o() ? (s.assignedSlot && (s = s.assignedSlot),
                    s.closest(e) || t(s.getRootNode().host)) : null
                }(t)
            }(u, p.target) : c.closest(u)[0]))
                return void (t.allowClick = !0);
            if (n.swipeHandler && !c.closest(n.swipeHandler)[0])
                return;
            l.currentX = "touchstart" === p.type ? p.targetTouches[0].pageX : p.pageX,
            l.currentY = "touchstart" === p.type ? p.targetTouches[0].pageY : p.pageY;
            const f = l.currentX
              , m = l.currentY
              , v = n.edgeSwipeDetection || n.iOSEdgeSwipeDetection
              , b = n.edgeSwipeThreshold || n.iOSEdgeSwipeThreshold;
            if (v && (f <= b || f >= i.innerWidth - b)) {
                if ("prevent" !== v)
                    return;
                e.preventDefault()
            }
            if (Object.assign(a, {
                isTouched: !0,
                isMoved: !1,
                allowTouchCallbacks: !0,
                isScrolling: void 0,
                startMoving: void 0
            }),
            l.startX = f,
            l.startY = m,
            a.touchStartTime = w(),
            t.allowClick = !0,
            t.updateSize(),
            t.swipeDirection = void 0,
            n.threshold > 0 && (a.allowThresholdMove = !1),
            "touchstart" !== p.type) {
                let e = !0;
                c.is(a.focusableElements) && (e = !1),
                s.activeElement && g(s.activeElement).is(a.focusableElements) && s.activeElement !== c[0] && s.activeElement.blur();
                const i = e && t.allowTouchMove && n.touchStartPreventDefault;
                !n.touchStartForcePreventDefault && !i || c[0].isContentEditable || p.preventDefault()
            }
            t.emit("touchStart", p)
        }
        function D(e) {
            const t = r()
              , s = this
              , i = s.touchEventsData
              , {params: a, touches: n, rtlTranslate: l, enabled: o} = s;
            if (!o)
                return;
            let d = e;
            if (d.originalEvent && (d = d.originalEvent),
            !i.isTouched)
                return void (i.startMoving && i.isScrolling && s.emit("touchMoveOpposite", d));
            if (i.isTouchEvent && "touchmove" !== d.type)
                return;
            const p = "touchmove" === d.type && d.targetTouches && (d.targetTouches[0] || d.changedTouches[0])
              , c = "touchmove" === d.type ? p.pageX : d.pageX
              , u = "touchmove" === d.type ? p.pageY : d.pageY;
            if (d.preventedByNestedSwiper)
                return n.startX = c,
                void (n.startY = u);
            if (!s.allowTouchMove)
                return s.allowClick = !1,
                void (i.isTouched && (Object.assign(n, {
                    startX: c,
                    startY: u,
                    currentX: c,
                    currentY: u
                }),
                i.touchStartTime = w()));
            if (i.isTouchEvent && a.touchReleaseOnEdges && !a.loop)
                if (s.isVertical()) {
                    if (u < n.startY && s.translate <= s.maxTranslate() || u > n.startY && s.translate >= s.minTranslate())
                        return i.isTouched = !1,
                        void (i.isMoved = !1)
                } else if (c < n.startX && s.translate <= s.maxTranslate() || c > n.startX && s.translate >= s.minTranslate())
                    return;
            if (i.isTouchEvent && t.activeElement && d.target === t.activeElement && g(d.target).is(i.focusableElements))
                return i.isMoved = !0,
                void (s.allowClick = !1);
            if (i.allowTouchCallbacks && s.emit("touchMove", d),
            d.targetTouches && d.targetTouches.length > 1)
                return;
            n.currentX = c,
            n.currentY = u;
            const h = n.currentX - n.startX
              , f = n.currentY - n.startY;
            if (s.params.threshold && Math.sqrt(h ** 2 + f ** 2) < s.params.threshold)
                return;
            if (void 0 === i.isScrolling) {
                let e;
                s.isHorizontal() && n.currentY === n.startY || s.isVertical() && n.currentX === n.startX ? i.isScrolling = !1 : h * h + f * f >= 25 && (e = 180 * Math.atan2(Math.abs(f), Math.abs(h)) / Math.PI,
                i.isScrolling = s.isHorizontal() ? e > a.touchAngle : 90 - e > a.touchAngle)
            }
            if (i.isScrolling && s.emit("touchMoveOpposite", d),
            void 0 === i.startMoving && (n.currentX === n.startX && n.currentY === n.startY || (i.startMoving = !0)),
            i.isScrolling)
                return void (i.isTouched = !1);
            if (!i.startMoving)
                return;
            s.allowClick = !1,
            !a.cssMode && d.cancelable && d.preventDefault(),
            a.touchMoveStopPropagation && !a.nested && d.stopPropagation(),
            i.isMoved || (a.loop && !a.cssMode && s.loopFix(),
            i.startTranslate = s.getTranslate(),
            s.setTransition(0),
            s.animating && s.$wrapperEl.trigger("webkitTransitionEnd transitionend"),
            i.allowMomentumBounce = !1,
            !a.grabCursor || !0 !== s.allowSlideNext && !0 !== s.allowSlidePrev || s.setGrabCursor(!0),
            s.emit("sliderFirstMove", d)),
            s.emit("sliderMove", d),
            i.isMoved = !0;
            let m = s.isHorizontal() ? h : f;
            n.diff = m,
            m *= a.touchRatio,
            l && (m = -m),
            s.swipeDirection = m > 0 ? "prev" : "next",
            i.currentTranslate = m + i.startTranslate;
            let v = !0
              , b = a.resistanceRatio;
            if (a.touchReleaseOnEdges && (b = 0),
            m > 0 && i.currentTranslate > s.minTranslate() ? (v = !1,
            a.resistance && (i.currentTranslate = s.minTranslate() - 1 + (-s.minTranslate() + i.startTranslate + m) ** b)) : m < 0 && i.currentTranslate < s.maxTranslate() && (v = !1,
            a.resistance && (i.currentTranslate = s.maxTranslate() + 1 - (s.maxTranslate() - i.startTranslate - m) ** b)),
            v && (d.preventedByNestedSwiper = !0),
            !s.allowSlideNext && "next" === s.swipeDirection && i.currentTranslate < i.startTranslate && (i.currentTranslate = i.startTranslate),
            !s.allowSlidePrev && "prev" === s.swipeDirection && i.currentTranslate > i.startTranslate && (i.currentTranslate = i.startTranslate),
            s.allowSlidePrev || s.allowSlideNext || (i.currentTranslate = i.startTranslate),
            a.threshold > 0) {
                if (!(Math.abs(m) > a.threshold || i.allowThresholdMove))
                    return void (i.currentTranslate = i.startTranslate);
                if (!i.allowThresholdMove)
                    return i.allowThresholdMove = !0,
                    n.startX = n.currentX,
                    n.startY = n.currentY,
                    i.currentTranslate = i.startTranslate,
                    void (n.diff = s.isHorizontal() ? n.currentX - n.startX : n.currentY - n.startY)
            }
            a.followFinger && !a.cssMode && ((a.freeMode && a.freeMode.enabled && s.freeMode || a.watchSlidesProgress) && (s.updateActiveIndex(),
            s.updateSlidesClasses()),
            s.params.freeMode && a.freeMode.enabled && s.freeMode && s.freeMode.onTouchMove(),
            s.updateProgress(i.currentTranslate),
            s.setTranslate(i.currentTranslate))
        }
        function G(e) {
            const t = this
              , s = t.touchEventsData
              , {params: i, touches: a, rtlTranslate: n, slidesGrid: r, enabled: l} = t;
            if (!l)
                return;
            let o = e;
            if (o.originalEvent && (o = o.originalEvent),
            s.allowTouchCallbacks && t.emit("touchEnd", o),
            s.allowTouchCallbacks = !1,
            !s.isTouched)
                return s.isMoved && i.grabCursor && t.setGrabCursor(!1),
                s.isMoved = !1,
                void (s.startMoving = !1);
            i.grabCursor && s.isMoved && s.isTouched && (!0 === t.allowSlideNext || !0 === t.allowSlidePrev) && t.setGrabCursor(!1);
            const d = w()
              , p = d - s.touchStartTime;
            if (t.allowClick) {
                const e = o.path || o.composedPath && o.composedPath();
                t.updateClickedSlide(e && e[0] || o.target),
                t.emit("tap click", o),
                p < 300 && d - s.lastClickTime < 300 && t.emit("doubleTap doubleClick", o)
            }
            if (s.lastClickTime = w(),
            v((()=>{
                t.destroyed || (t.allowClick = !0)
            }
            )),
            !s.isTouched || !s.isMoved || !t.swipeDirection || 0 === a.diff || s.currentTranslate === s.startTranslate)
                return s.isTouched = !1,
                s.isMoved = !1,
                void (s.startMoving = !1);
            let c;
            if (s.isTouched = !1,
            s.isMoved = !1,
            s.startMoving = !1,
            c = i.followFinger ? n ? t.translate : -t.translate : -s.currentTranslate,
            i.cssMode)
                return;
            if (t.params.freeMode && i.freeMode.enabled)
                return void t.freeMode.onTouchEnd({
                    currentPos: c
                });
            let u = 0
              , h = t.slidesSizesGrid[0];
            for (let e = 0; e < r.length; e += e < i.slidesPerGroupSkip ? 1 : i.slidesPerGroup) {
                const t = e < i.slidesPerGroupSkip - 1 ? 1 : i.slidesPerGroup;
                void 0 !== r[e + t] ? c >= r[e] && c < r[e + t] && (u = e,
                h = r[e + t] - r[e]) : c >= r[e] && (u = e,
                h = r[r.length - 1] - r[r.length - 2])
            }
            const f = (c - r[u]) / h
              , m = u < i.slidesPerGroupSkip - 1 ? 1 : i.slidesPerGroup;
            if (p > i.longSwipesMs) {
                if (!i.longSwipes)
                    return void t.slideTo(t.activeIndex);
                "next" === t.swipeDirection && (f >= i.longSwipesRatio ? t.slideTo(u + m) : t.slideTo(u)),
                "prev" === t.swipeDirection && (f > 1 - i.longSwipesRatio ? t.slideTo(u + m) : t.slideTo(u))
            } else {
                if (!i.shortSwipes)
                    return void t.slideTo(t.activeIndex);
                !t.navigation || o.target !== t.navigation.nextEl && o.target !== t.navigation.prevEl ? ("next" === t.swipeDirection && t.slideTo(u + m),
                "prev" === t.swipeDirection && t.slideTo(u)) : o.target === t.navigation.nextEl ? t.slideTo(u + m) : t.slideTo(u)
            }
        }
        function B() {
            const e = this
              , {params: t, el: s} = e;
            if (s && 0 === s.offsetWidth)
                return;
            t.breakpoints && e.setBreakpoint();
            const {allowSlideNext: i, allowSlidePrev: a, snapGrid: n} = e;
            e.allowSlideNext = !0,
            e.allowSlidePrev = !0,
            e.updateSize(),
            e.updateSlides(),
            e.updateSlidesClasses(),
            ("auto" === t.slidesPerView || t.slidesPerView > 1) && e.isEnd && !e.isBeginning && !e.params.centeredSlides ? e.slideTo(e.slides.length - 1, 0, !1, !0) : e.slideTo(e.activeIndex, 0, !1, !0),
            e.autoplay && e.autoplay.running && e.autoplay.paused && e.autoplay.run(),
            e.allowSlidePrev = a,
            e.allowSlideNext = i,
            e.params.watchOverflow && n !== e.snapGrid && e.checkOverflow()
        }
        function N(e) {
            const t = this;
            t.enabled && (t.allowClick || (t.params.preventClicks && e.preventDefault(),
            t.params.preventClicksPropagation && t.animating && (e.stopPropagation(),
            e.stopImmediatePropagation())))
        }
        function _() {
            const e = this
              , {wrapperEl: t, rtlTranslate: s, enabled: i} = e;
            if (!i)
                return;
            let a;
            e.previousTranslate = e.translate,
            e.isHorizontal() ? e.translate = -t.scrollLeft : e.translate = -t.scrollTop,
            -0 === e.translate && (e.translate = 0),
            e.updateActiveIndex(),
            e.updateSlidesClasses();
            const n = e.maxTranslate() - e.minTranslate();
            a = 0 === n ? 0 : (e.translate - e.minTranslate()) / n,
            a !== e.progress && e.updateProgress(s ? -e.translate : e.translate),
            e.emit("setTranslate", e.translate, !1)
        }
        let H = !1;
        function F() {}
        const j = (e,t)=>{
            const s = r()
              , {params: i, touchEvents: a, el: n, wrapperEl: l, device: o, support: d} = e
              , p = !!i.nested
              , c = "on" === t ? "addEventListener" : "removeEventListener"
              , u = t;
            if (d.touch) {
                const t = !("touchstart" !== a.start || !d.passiveListener || !i.passiveListeners) && {
                    passive: !0,
                    capture: !1
                };
                n[c](a.start, e.onTouchStart, t),
                n[c](a.move, e.onTouchMove, d.passiveListener ? {
                    passive: !1,
                    capture: p
                } : p),
                n[c](a.end, e.onTouchEnd, t),
                a.cancel && n[c](a.cancel, e.onTouchEnd, t)
            } else
                n[c](a.start, e.onTouchStart, !1),
                s[c](a.move, e.onTouchMove, p),
                s[c](a.end, e.onTouchEnd, !1);
            (i.preventClicks || i.preventClicksPropagation) && n[c]("click", e.onClick, !0),
            i.cssMode && l[c]("scroll", e.onScroll),
            i.updateOnWindowResize ? e[u](o.ios || o.android ? "resize orientationchange observerUpdate" : "resize observerUpdate", B, !0) : e[u]("observerUpdate", B, !0)
        }
        ;
        var V = {
            attachEvents: function() {
                const e = this
                  , t = r()
                  , {params: s, support: i} = e;
                e.onTouchStart = A.bind(e),
                e.onTouchMove = D.bind(e),
                e.onTouchEnd = G.bind(e),
                s.cssMode && (e.onScroll = _.bind(e)),
                e.onClick = N.bind(e),
                i.touch && !H && (t.addEventListener("touchstart", F),
                H = !0),
                j(e, "on")
            },
            detachEvents: function() {
                j(this, "off")
            }
        };
        const R = (e,t)=>e.grid && t.grid && t.grid.rows > 1;
        s(5137);
        var W = {
            addClasses: function() {
                const e = this
                  , {classNames: t, params: s, rtl: i, $el: a, device: n, support: r} = e
                  , l = function(e, t) {
                    const s = [];
                    return e.forEach((e=>{
                        "object" == typeof e ? Object.keys(e).forEach((i=>{
                            e[i] && s.push(t + i)
                        }
                        )) : "string" == typeof e && s.push(t + e)
                    }
                    )),
                    s
                }(["initialized", s.direction, {
                    "pointer-events": !r.touch
                }, {
                    "free-mode": e.params.freeMode && s.freeMode.enabled
                }, {
                    autoheight: s.autoHeight
                }, {
                    rtl: i
                }, {
                    grid: s.grid && s.grid.rows > 1
                }, {
                    "grid-column": s.grid && s.grid.rows > 1 && "column" === s.grid.fill
                }, {
                    android: n.android
                }, {
                    ios: n.ios
                }, {
                    "css-mode": s.cssMode
                }, {
                    centered: s.cssMode && s.centeredSlides
                }], s.containerModifierClass);
                t.push(...l),
                a.addClass([...t].join(" ")),
                e.emitContainerClasses()
            },
            removeClasses: function() {
                const {$el: e, classNames: t} = this;
                e.removeClass(t.join(" ")),
                this.emitContainerClasses()
            }
        }
          , q = {
            init: !0,
            direction: "horizontal",
            touchEventsTarget: "wrapper",
            initialSlide: 0,
            speed: 300,
            cssMode: !1,
            updateOnWindowResize: !0,
            resizeObserver: !0,
            nested: !1,
            createElements: !1,
            enabled: !0,
            focusableElements: "input, select, option, textarea, button, video, label",
            width: null,
            height: null,
            preventInteractionOnTransition: !1,
            userAgent: null,
            url: null,
            edgeSwipeDetection: !1,
            edgeSwipeThreshold: 20,
            autoHeight: !1,
            setWrapperSize: !1,
            virtualTranslate: !1,
            effect: "slide",
            breakpoints: void 0,
            breakpointsBase: "window",
            spaceBetween: 0,
            slidesPerView: 1,
            slidesPerGroup: 1,
            slidesPerGroupSkip: 0,
            slidesPerGroupAuto: !1,
            centeredSlides: !1,
            centeredSlidesBounds: !1,
            slidesOffsetBefore: 0,
            slidesOffsetAfter: 0,
            normalizeSlideIndex: !0,
            centerInsufficientSlides: !1,
            watchOverflow: !0,
            roundLengths: !1,
            touchRatio: 1,
            touchAngle: 45,
            simulateTouch: !0,
            shortSwipes: !0,
            longSwipes: !0,
            longSwipesRatio: .5,
            longSwipesMs: 300,
            followFinger: !0,
            allowTouchMove: !0,
            threshold: 0,
            touchMoveStopPropagation: !1,
            touchStartPreventDefault: !0,
            touchStartForcePreventDefault: !1,
            touchReleaseOnEdges: !1,
            uniqueNavElements: !0,
            resistance: !0,
            resistanceRatio: .85,
            watchSlidesProgress: !1,
            grabCursor: !1,
            preventClicks: !0,
            preventClicksPropagation: !0,
            slideToClickedSlide: !1,
            preloadImages: !0,
            updateOnImagesReady: !0,
            loop: !1,
            loopAdditionalSlides: 0,
            loopedSlides: null,
            loopFillGroupWithBlank: !1,
            loopPreventsSlide: !0,
            rewind: !1,
            allowSlidePrev: !0,
            allowSlideNext: !0,
            swipeHandler: null,
            noSwiping: !0,
            noSwipingClass: "swiper-no-swiping",
            noSwipingSelector: null,
            passiveListeners: !0,
            containerModifierClass: "swiper-",
            slideClass: "swiper-slide",
            slideBlankClass: "swiper-slide-invisible-blank",
            slideActiveClass: "swiper-slide-active",
            slideDuplicateActiveClass: "swiper-slide-duplicate-active",
            slideVisibleClass: "swiper-slide-visible",
            slideDuplicateClass: "swiper-slide-duplicate",
            slideNextClass: "swiper-slide-next",
            slideDuplicateNextClass: "swiper-slide-duplicate-next",
            slidePrevClass: "swiper-slide-prev",
            slideDuplicatePrevClass: "swiper-slide-duplicate-prev",
            wrapperClass: "swiper-wrapper",
            runCallbacksOnInit: !0,
            _emitClasses: !1
        };
        function X(e, t) {
            return function(s={}) {
                const i = Object.keys(s)[0]
                  , a = s[i];
                "object" == typeof a && null !== a ? (["navigation", "pagination", "scrollbar"].indexOf(i) >= 0 && !0 === e[i] && (e[i] = {
                    auto: !0
                }),
                i in e && "enabled"in a ? (!0 === e[i] && (e[i] = {
                    enabled: !0
                }),
                "object" != typeof e[i] || "enabled"in e[i] || (e[i].enabled = !0),
                e[i] || (e[i] = {
                    enabled: !1
                }),
                C(t, s)) : C(t, s)) : C(t, s)
            }
        }
        const Y = {
            eventsEmitter: M,
            update: k,
            translate: P,
            transition: O,
            slide: z,
            loop: I,
            grabCursor: {
                setGrabCursor: function(e) {
                    const t = this;
                    if (t.support.touch || !t.params.simulateTouch || t.params.watchOverflow && t.isLocked || t.params.cssMode)
                        return;
                    const s = "container" === t.params.touchEventsTarget ? t.el : t.wrapperEl;
                    s.style.cursor = "move",
                    s.style.cursor = e ? "-webkit-grabbing" : "-webkit-grab",
                    s.style.cursor = e ? "-moz-grabbin" : "-moz-grab",
                    s.style.cursor = e ? "grabbing" : "grab"
                },
                unsetGrabCursor: function() {
                    const e = this;
                    e.support.touch || e.params.watchOverflow && e.isLocked || e.params.cssMode || (e["container" === e.params.touchEventsTarget ? "el" : "wrapperEl"].style.cursor = "")
                }
            },
            events: V,
            breakpoints: {
                setBreakpoint: function() {
                    const e = this
                      , {activeIndex: t, initialized: s, loopedSlides: i=0, params: a, $el: n} = e
                      , r = a.breakpoints;
                    if (!r || r && 0 === Object.keys(r).length)
                        return;
                    const l = e.getBreakpoint(r, e.params.breakpointsBase, e.el);
                    if (!l || e.currentBreakpoint === l)
                        return;
                    const o = (l in r ? r[l] : void 0) || e.originalParams
                      , d = R(e, a)
                      , p = R(e, o)
                      , c = a.enabled;
                    d && !p ? (n.removeClass(`${a.containerModifierClass}grid ${a.containerModifierClass}grid-column`),
                    e.emitContainerClasses()) : !d && p && (n.addClass(`${a.containerModifierClass}grid`),
                    (o.grid.fill && "column" === o.grid.fill || !o.grid.fill && "column" === a.grid.fill) && n.addClass(`${a.containerModifierClass}grid-column`),
                    e.emitContainerClasses());
                    const u = o.direction && o.direction !== a.direction
                      , h = a.loop && (o.slidesPerView !== a.slidesPerView || u);
                    u && s && e.changeDirection(),
                    C(e.params, o);
                    const f = e.params.enabled;
                    Object.assign(e, {
                        allowTouchMove: e.params.allowTouchMove,
                        allowSlideNext: e.params.allowSlideNext,
                        allowSlidePrev: e.params.allowSlidePrev
                    }),
                    c && !f ? e.disable() : !c && f && e.enable(),
                    e.currentBreakpoint = l,
                    e.emit("_beforeBreakpoint", o),
                    h && s && (e.loopDestroy(),
                    e.loopCreate(),
                    e.updateSlides(),
                    e.slideTo(t - i + e.loopedSlides, 0, !1)),
                    e.emit("breakpoint", o)
                },
                getBreakpoint: function(e, t="window", s) {
                    if (!e || "container" === t && !s)
                        return;
                    let i = !1;
                    const a = o()
                      , n = "window" === t ? a.innerHeight : s.clientHeight
                      , r = Object.keys(e).map((e=>{
                        if ("string" == typeof e && 0 === e.indexOf("@")) {
                            const t = parseFloat(e.substr(1));
                            return {
                                value: n * t,
                                point: e
                            }
                        }
                        return {
                            value: e,
                            point: e
                        }
                    }
                    ));
                    r.sort(((e,t)=>parseInt(e.value, 10) - parseInt(t.value, 10)));
                    for (let e = 0; e < r.length; e += 1) {
                        const {point: n, value: l} = r[e];
                        "window" === t ? a.matchMedia(`(min-width: ${l}px)`).matches && (i = n) : l <= s.clientWidth && (i = n)
                    }
                    return i || "max"
                }
            },
            checkOverflow: {
                checkOverflow: function() {
                    const e = this
                      , {isLocked: t, params: s} = e
                      , {slidesOffsetBefore: i} = s;
                    if (i) {
                        const t = e.slides.length - 1
                          , s = e.slidesGrid[t] + e.slidesSizesGrid[t] + 2 * i;
                        e.isLocked = e.size > s
                    } else
                        e.isLocked = 1 === e.snapGrid.length;
                    !0 === s.allowSlideNext && (e.allowSlideNext = !e.isLocked),
                    !0 === s.allowSlidePrev && (e.allowSlidePrev = !e.isLocked),
                    t && t !== e.isLocked && (e.isEnd = !1),
                    t !== e.isLocked && e.emit(e.isLocked ? "lock" : "unlock")
                }
            },
            classes: W,
            images: {
                loadImage: function(e, t, s, i, a, n) {
                    const r = o();
                    let l;
                    function d() {
                        n && n()
                    }
                    g(e).parent("picture")[0] || e.complete && a ? d() : t ? (l = new r.Image,
                    l.onload = d,
                    l.onerror = d,
                    i && (l.sizes = i),
                    s && (l.srcset = s),
                    t && (l.src = t)) : d()
                },
                preloadImages: function() {
                    const e = this;
                    function t() {
                        null != e && e && !e.destroyed && (void 0 !== e.imagesLoaded && (e.imagesLoaded += 1),
                        e.imagesLoaded === e.imagesToLoad.length && (e.params.updateOnImagesReady && e.update(),
                        e.emit("imagesReady")))
                    }
                    e.imagesToLoad = e.$el.find("img");
                    for (let s = 0; s < e.imagesToLoad.length; s += 1) {
                        const i = e.imagesToLoad[s];
                        e.loadImage(i, i.currentSrc || i.getAttribute("src"), i.srcset || i.getAttribute("srcset"), i.sizes || i.getAttribute("sizes"), !0, t)
                    }
                }
            }
        }
          , U = {};
        class K {
            constructor(...e) {
                let t, s;
                if (1 === e.length && e[0].constructor && "Object" === Object.prototype.toString.call(e[0]).slice(8, -1) ? s = e[0] : [t,s] = e,
                s || (s = {}),
                s = C({}, s),
                t && !s.el && (s.el = t),
                s.el && g(s.el).length > 1) {
                    const e = [];
                    return g(s.el).each((t=>{
                        const i = C({}, s, {
                            el: t
                        });
                        e.push(new K(i))
                    }
                    )),
                    e
                }
                const i = this;
                i.__swiper__ = !0,
                i.support = $(),
                i.device = function(e={}) {
                    return S || (S = function({userAgent: e}={}) {
                        const t = $()
                          , s = o()
                          , i = s.navigator.platform
                          , a = e || s.navigator.userAgent
                          , n = {
                            ios: !1,
                            android: !1
                        }
                          , r = s.screen.width
                          , l = s.screen.height
                          , d = a.match(/(Android);?[\s\/]+([\d.]+)?/);
                        let p = a.match(/(iPad).*OS\s([\d_]+)/);
                        const c = a.match(/(iPod)(.*OS\s([\d_]+))?/)
                          , u = !p && a.match(/(iPhone\sOS|iOS)\s([\d_]+)/)
                          , h = "Win32" === i;
                        let f = "MacIntel" === i;
                        return !p && f && t.touch && ["1024x1366", "1366x1024", "834x1194", "1194x834", "834x1112", "1112x834", "768x1024", "1024x768", "820x1180", "1180x820", "810x1080", "1080x810"].indexOf(`${r}x${l}`) >= 0 && (p = a.match(/(Version)\/([\d.]+)/),
                        p || (p = [0, 1, "13_0_0"]),
                        f = !1),
                        d && !h && (n.os = "android",
                        n.android = !0),
                        (p || u || c) && (n.os = "ios",
                        n.ios = !0),
                        n
                    }(e)),
                    S
                }({
                    userAgent: s.userAgent
                }),
                i.browser = (E || (E = function() {
                    const e = o();
                    return {
                        isSafari: function() {
                            const t = e.navigator.userAgent.toLowerCase();
                            return t.indexOf("safari") >= 0 && t.indexOf("chrome") < 0 && t.indexOf("android") < 0
                        }(),
                        isWebView: /(iPhone|iPod|iPad).*AppleWebKit(?!.*Safari)/i.test(e.navigator.userAgent)
                    }
                }()),
                E),
                i.eventsListeners = {},
                i.eventsAnyListeners = [],
                i.modules = [...i.__modules__],
                s.modules && Array.isArray(s.modules) && i.modules.push(...s.modules);
                const a = {};
                i.modules.forEach((e=>{
                    e({
                        swiper: i,
                        extendParams: X(s, a),
                        on: i.on.bind(i),
                        once: i.once.bind(i),
                        off: i.off.bind(i),
                        emit: i.emit.bind(i)
                    })
                }
                ));
                const n = C({}, q, a);
                return i.params = C({}, n, U, s),
                i.originalParams = C({}, i.params),
                i.passedParams = C({}, s),
                i.params && i.params.on && Object.keys(i.params.on).forEach((e=>{
                    i.on(e, i.params.on[e])
                }
                )),
                i.params && i.params.onAny && i.onAny(i.params.onAny),
                i.$ = g,
                Object.assign(i, {
                    enabled: i.params.enabled,
                    el: t,
                    classNames: [],
                    slides: g(),
                    slidesGrid: [],
                    snapGrid: [],
                    slidesSizesGrid: [],
                    isHorizontal: ()=>"horizontal" === i.params.direction,
                    isVertical: ()=>"vertical" === i.params.direction,
                    activeIndex: 0,
                    realIndex: 0,
                    isBeginning: !0,
                    isEnd: !1,
                    translate: 0,
                    previousTranslate: 0,
                    progress: 0,
                    velocity: 0,
                    animating: !1,
                    allowSlideNext: i.params.allowSlideNext,
                    allowSlidePrev: i.params.allowSlidePrev,
                    touchEvents: function() {
                        const e = ["touchstart", "touchmove", "touchend", "touchcancel"]
                          , t = ["pointerdown", "pointermove", "pointerup"];
                        return i.touchEventsTouch = {
                            start: e[0],
                            move: e[1],
                            end: e[2],
                            cancel: e[3]
                        },
                        i.touchEventsDesktop = {
                            start: t[0],
                            move: t[1],
                            end: t[2]
                        },
                        i.support.touch || !i.params.simulateTouch ? i.touchEventsTouch : i.touchEventsDesktop
                    }(),
                    touchEventsData: {
                        isTouched: void 0,
                        isMoved: void 0,
                        allowTouchCallbacks: void 0,
                        touchStartTime: void 0,
                        isScrolling: void 0,
                        currentTranslate: void 0,
                        startTranslate: void 0,
                        allowThresholdMove: void 0,
                        focusableElements: i.params.focusableElements,
                        lastClickTime: w(),
                        clickTimeout: void 0,
                        velocities: [],
                        allowMomentumBounce: void 0,
                        isTouchEvent: void 0,
                        startMoving: void 0
                    },
                    allowClick: !0,
                    allowTouchMove: i.params.allowTouchMove,
                    touches: {
                        startX: 0,
                        startY: 0,
                        currentX: 0,
                        currentY: 0,
                        diff: 0
                    },
                    imagesToLoad: [],
                    imagesLoaded: 0
                }),
                i.emit("_swiper"),
                i.params.init && i.init(),
                i
            }
            enable() {
                const e = this;
                e.enabled || (e.enabled = !0,
                e.params.grabCursor && e.setGrabCursor(),
                e.emit("enable"))
            }
            disable() {
                const e = this;
                e.enabled && (e.enabled = !1,
                e.params.grabCursor && e.unsetGrabCursor(),
                e.emit("disable"))
            }
            setProgress(e, t) {
                const s = this;
                e = Math.min(Math.max(e, 0), 1);
                const i = s.minTranslate()
                  , a = (s.maxTranslate() - i) * e + i;
                s.translateTo(a, void 0 === t ? 0 : t),
                s.updateActiveIndex(),
                s.updateSlidesClasses()
            }
            emitContainerClasses() {
                const e = this;
                if (!e.params._emitClasses || !e.el)
                    return;
                const t = e.el.className.split(" ").filter((t=>0 === t.indexOf("swiper") || 0 === t.indexOf(e.params.containerModifierClass)));
                e.emit("_containerClasses", t.join(" "))
            }
            getSlideClasses(e) {
                const t = this;
                return e.className.split(" ").filter((e=>0 === e.indexOf("swiper-slide") || 0 === e.indexOf(t.params.slideClass))).join(" ")
            }
            emitSlidesClasses() {
                const e = this;
                if (!e.params._emitClasses || !e.el)
                    return;
                const t = [];
                e.slides.each((s=>{
                    const i = e.getSlideClasses(s);
                    t.push({
                        slideEl: s,
                        classNames: i
                    }),
                    e.emit("_slideClass", s, i)
                }
                )),
                e.emit("_slideClasses", t)
            }
            slidesPerViewDynamic(e="current", t=!1) {
                const {params: s, slides: i, slidesGrid: a, slidesSizesGrid: n, size: r, activeIndex: l} = this;
                let o = 1;
                if (s.centeredSlides) {
                    let e, t = i[l].swiperSlideSize;
                    for (let s = l + 1; s < i.length; s += 1)
                        i[s] && !e && (t += i[s].swiperSlideSize,
                        o += 1,
                        t > r && (e = !0));
                    for (let s = l - 1; s >= 0; s -= 1)
                        i[s] && !e && (t += i[s].swiperSlideSize,
                        o += 1,
                        t > r && (e = !0))
                } else if ("current" === e)
                    for (let e = l + 1; e < i.length; e += 1)
                        (t ? a[e] + n[e] - a[l] < r : a[e] - a[l] < r) && (o += 1);
                else
                    for (let e = l - 1; e >= 0; e -= 1)
                        a[l] - a[e] < r && (o += 1);
                return o
            }
            update() {
                const e = this;
                if (!e || e.destroyed)
                    return;
                const {snapGrid: t, params: s} = e;
                function i() {
                    const t = e.rtlTranslate ? -1 * e.translate : e.translate
                      , s = Math.min(Math.max(t, e.maxTranslate()), e.minTranslate());
                    e.setTranslate(s),
                    e.updateActiveIndex(),
                    e.updateSlidesClasses()
                }
                let a;
                s.breakpoints && e.setBreakpoint(),
                e.updateSize(),
                e.updateSlides(),
                e.updateProgress(),
                e.updateSlidesClasses(),
                e.params.freeMode && e.params.freeMode.enabled ? (i(),
                e.params.autoHeight && e.updateAutoHeight()) : (a = ("auto" === e.params.slidesPerView || e.params.slidesPerView > 1) && e.isEnd && !e.params.centeredSlides ? e.slideTo(e.slides.length - 1, 0, !1, !0) : e.slideTo(e.activeIndex, 0, !1, !0),
                a || i()),
                s.watchOverflow && t !== e.snapGrid && e.checkOverflow(),
                e.emit("update")
            }
            changeDirection(e, t=!0) {
                const s = this
                  , i = s.params.direction;
                return e || (e = "horizontal" === i ? "vertical" : "horizontal"),
                e === i || "horizontal" !== e && "vertical" !== e || (s.$el.removeClass(`${s.params.containerModifierClass}${i}`).addClass(`${s.params.containerModifierClass}${e}`),
                s.emitContainerClasses(),
                s.params.direction = e,
                s.slides.each((t=>{
                    "vertical" === e ? t.style.width = "" : t.style.height = ""
                }
                )),
                s.emit("changeDirection"),
                t && s.update()),
                s
            }
            mount(e) {
                const t = this;
                if (t.mounted)
                    return !0;
                const s = g(e || t.params.el);
                if (!(e = s[0]))
                    return !1;
                e.swiper = t;
                const i = ()=>`.${(t.params.wrapperClass || "").trim().split(" ").join(".")}`;
                let a = (()=>{
                    if (e && e.shadowRoot && e.shadowRoot.querySelector) {
                        const t = g(e.shadowRoot.querySelector(i()));
                        return t.children = e=>s.children(e),
                        t
                    }
                    return s.children(i())
                }
                )();
                if (0 === a.length && t.params.createElements) {
                    const e = r().createElement("div");
                    a = g(e),
                    e.className = t.params.wrapperClass,
                    s.append(e),
                    s.children(`.${t.params.slideClass}`).each((e=>{
                        a.append(e)
                    }
                    ))
                }
                return Object.assign(t, {
                    $el: s,
                    el: e,
                    $wrapperEl: a,
                    wrapperEl: a[0],
                    mounted: !0,
                    rtl: "rtl" === e.dir.toLowerCase() || "rtl" === s.css("direction"),
                    rtlTranslate: "horizontal" === t.params.direction && ("rtl" === e.dir.toLowerCase() || "rtl" === s.css("direction")),
                    wrongRTL: "-webkit-box" === a.css("display")
                }),
                !0
            }
            init(e) {
                const t = this;
                return t.initialized || !1 === t.mount(e) || (t.emit("beforeInit"),
                t.params.breakpoints && t.setBreakpoint(),
                t.addClasses(),
                t.params.loop && t.loopCreate(),
                t.updateSize(),
                t.updateSlides(),
                t.params.watchOverflow && t.checkOverflow(),
                t.params.grabCursor && t.enabled && t.setGrabCursor(),
                t.params.preloadImages && t.preloadImages(),
                t.params.loop ? t.slideTo(t.params.initialSlide + t.loopedSlides, 0, t.params.runCallbacksOnInit, !1, !0) : t.slideTo(t.params.initialSlide, 0, t.params.runCallbacksOnInit, !1, !0),
                t.attachEvents(),
                t.initialized = !0,
                t.emit("init"),
                t.emit("afterInit")),
                t
            }
            destroy(e=!0, t=!0) {
                const s = this
                  , {params: i, $el: a, $wrapperEl: n, slides: r} = s;
                return void 0 === s.params || s.destroyed || (s.emit("beforeDestroy"),
                s.initialized = !1,
                s.detachEvents(),
                i.loop && s.loopDestroy(),
                t && (s.removeClasses(),
                a.removeAttr("style"),
                n.removeAttr("style"),
                r && r.length && r.removeClass([i.slideVisibleClass, i.slideActiveClass, i.slideNextClass, i.slidePrevClass].join(" ")).removeAttr("style").removeAttr("data-swiper-slide-index")),
                s.emit("destroy"),
                Object.keys(s.eventsListeners).forEach((e=>{
                    s.off(e)
                }
                )),
                !1 !== e && (s.$el[0].swiper = null,
                function(e) {
                    const t = e;
                    Object.keys(t).forEach((e=>{
                        try {
                            t[e] = null
                        } catch (e) {}
                        try {
                            delete t[e]
                        } catch (e) {}
                    }
                    ))
                }(s)),
                s.destroyed = !0),
                null
            }
            static extendDefaults(e) {
                C(U, e)
            }
            static get extendedDefaults() {
                return U
            }
            static get defaults() {
                return q
            }
            static installModule(e) {
                K.prototype.__modules__ || (K.prototype.__modules__ = []);
                const t = K.prototype.__modules__;
                "function" == typeof e && t.indexOf(e) < 0 && t.push(e)
            }
            static use(e) {
                return Array.isArray(e) ? (e.forEach((e=>K.installModule(e))),
                K) : (K.installModule(e),
                K)
            }
        }
        Object.keys(Y).forEach((e=>{
            Object.keys(Y[e]).forEach((t=>{
                K.prototype[t] = Y[e][t]
            }
            ))
        }
        )),
        K.use([function({swiper: e, on: t, emit: s}) {
            const i = o();
            let a = null;
            const n = ()=>{
                e && !e.destroyed && e.initialized && (s("beforeResize"),
                s("resize"))
            }
              , r = ()=>{
                e && !e.destroyed && e.initialized && s("orientationchange")
            }
            ;
            t("init", (()=>{
                e.params.resizeObserver && void 0 !== i.ResizeObserver ? e && !e.destroyed && e.initialized && (a = new ResizeObserver((t=>{
                    const {width: s, height: i} = e;
                    let a = s
                      , r = i;
                    t.forEach((({contentBoxSize: t, contentRect: s, target: i})=>{
                        i && i !== e.el || (a = s ? s.width : (t[0] || t).inlineSize,
                        r = s ? s.height : (t[0] || t).blockSize)
                    }
                    )),
                    a === s && r === i || n()
                }
                )),
                a.observe(e.el)) : (i.addEventListener("resize", n),
                i.addEventListener("orientationchange", r))
            }
            )),
            t("destroy", (()=>{
                a && a.unobserve && e.el && (a.unobserve(e.el),
                a = null),
                i.removeEventListener("resize", n),
                i.removeEventListener("orientationchange", r)
            }
            ))
        }
        , function({swiper: e, extendParams: t, on: s, emit: i}) {
            const a = []
              , n = o()
              , r = (e,t={})=>{
                const s = new (n.MutationObserver || n.WebkitMutationObserver)((e=>{
                    if (1 === e.length)
                        return void i("observerUpdate", e[0]);
                    const t = function() {
                        i("observerUpdate", e[0])
                    };
                    n.requestAnimationFrame ? n.requestAnimationFrame(t) : n.setTimeout(t, 0)
                }
                ));
                s.observe(e, {
                    attributes: void 0 === t.attributes || t.attributes,
                    childList: void 0 === t.childList || t.childList,
                    characterData: void 0 === t.characterData || t.characterData
                }),
                a.push(s)
            }
            ;
            t({
                observer: !1,
                observeParents: !1,
                observeSlideChildren: !1
            }),
            s("init", (()=>{
                if (e.params.observer) {
                    if (e.params.observeParents) {
                        const t = e.$el.parents();
                        for (let e = 0; e < t.length; e += 1)
                            r(t[e])
                    }
                    r(e.$el[0], {
                        childList: e.params.observeSlideChildren
                    }),
                    r(e.$wrapperEl[0], {
                        attributes: !1
                    })
                }
            }
            )),
            s("destroy", (()=>{
                a.forEach((e=>{
                    e.disconnect()
                }
                )),
                a.splice(0, a.length)
            }
            ))
        }
        ]);
        var J = K;
        function Q(e, t, s, i) {
            const a = r();
            return e.params.createElements && Object.keys(i).forEach((n=>{
                if (!s[n] && !0 === s.auto) {
                    let r = e.$el.children(`.${i[n]}`)[0];
                    r || (r = a.createElement("div"),
                    r.className = i[n],
                    e.$el.append(r)),
                    s[n] = r,
                    t[n] = r
                }
            }
            )),
            s
        }
        function Z({swiper: e, extendParams: t, on: s, emit: i}) {
            function a(t) {
                let s;
                return t && (s = g(t),
                e.params.uniqueNavElements && "string" == typeof t && s.length > 1 && 1 === e.$el.find(t).length && (s = e.$el.find(t))),
                s
            }
            function n(t, s) {
                const i = e.params.navigation;
                t && t.length > 0 && (t[s ? "addClass" : "removeClass"](i.disabledClass),
                t[0] && "BUTTON" === t[0].tagName && (t[0].disabled = s),
                e.params.watchOverflow && e.enabled && t[e.isLocked ? "addClass" : "removeClass"](i.lockClass))
            }
            function r() {
                if (e.params.loop)
                    return;
                const {$nextEl: t, $prevEl: s} = e.navigation;
                n(s, e.isBeginning && !e.params.rewind),
                n(t, e.isEnd && !e.params.rewind)
            }
            function l(t) {
                t.preventDefault(),
                (!e.isBeginning || e.params.loop || e.params.rewind) && e.slidePrev()
            }
            function o(t) {
                t.preventDefault(),
                (!e.isEnd || e.params.loop || e.params.rewind) && e.slideNext()
            }
            function d() {
                const t = e.params.navigation;
                if (e.params.navigation = Q(e, e.originalParams.navigation, e.params.navigation, {
                    nextEl: "swiper-button-next",
                    prevEl: "swiper-button-prev"
                }),
                !t.nextEl && !t.prevEl)
                    return;
                const s = a(t.nextEl)
                  , i = a(t.prevEl);
                s && s.length > 0 && s.on("click", o),
                i && i.length > 0 && i.on("click", l),
                Object.assign(e.navigation, {
                    $nextEl: s,
                    nextEl: s && s[0],
                    $prevEl: i,
                    prevEl: i && i[0]
                }),
                e.enabled || (s && s.addClass(t.lockClass),
                i && i.addClass(t.lockClass))
            }
            function p() {
                const {$nextEl: t, $prevEl: s} = e.navigation;
                t && t.length && (t.off("click", o),
                t.removeClass(e.params.navigation.disabledClass)),
                s && s.length && (s.off("click", l),
                s.removeClass(e.params.navigation.disabledClass))
            }
            t({
                navigation: {
                    nextEl: null,
                    prevEl: null,
                    hideOnClick: !1,
                    disabledClass: "swiper-button-disabled",
                    hiddenClass: "swiper-button-hidden",
                    lockClass: "swiper-button-lock"
                }
            }),
            e.navigation = {
                nextEl: null,
                $nextEl: null,
                prevEl: null,
                $prevEl: null
            },
            s("init", (()=>{
                d(),
                r()
            }
            )),
            s("toEdge fromEdge lock unlock", (()=>{
                r()
            }
            )),
            s("destroy", (()=>{
                p()
            }
            )),
            s("enable disable", (()=>{
                const {$nextEl: t, $prevEl: s} = e.navigation;
                t && t[e.enabled ? "removeClass" : "addClass"](e.params.navigation.lockClass),
                s && s[e.enabled ? "removeClass" : "addClass"](e.params.navigation.lockClass)
            }
            )),
            s("click", ((t,s)=>{
                const {$nextEl: a, $prevEl: n} = e.navigation
                  , r = s.target;
                if (e.params.navigation.hideOnClick && !g(r).is(n) && !g(r).is(a)) {
                    if (e.pagination && e.params.pagination && e.params.pagination.clickable && (e.pagination.el === r || e.pagination.el.contains(r)))
                        return;
                    let t;
                    a ? t = a.hasClass(e.params.navigation.hiddenClass) : n && (t = n.hasClass(e.params.navigation.hiddenClass)),
                    i(!0 === t ? "navigationShow" : "navigationHide"),
                    a && a.toggleClass(e.params.navigation.hiddenClass),
                    n && n.toggleClass(e.params.navigation.hiddenClass)
                }
            }
            )),
            Object.assign(e.navigation, {
                update: r,
                init: d,
                destroy: p
            })
        }
        function ee(e="") {
            return `.${e.trim().replace(/([\.:!\/])/g, "\\$1").replace(/ /g, ".")}`
        }
        function te({swiper: e, extendParams: t, on: s, emit: i}) {
            const a = "swiper-pagination";
            let n;
            t({
                pagination: {
                    el: null,
                    bulletElement: "span",
                    clickable: !1,
                    hideOnClick: !1,
                    renderBullet: null,
                    renderProgressbar: null,
                    renderFraction: null,
                    renderCustom: null,
                    progressbarOpposite: !1,
                    type: "bullets",
                    dynamicBullets: !1,
                    dynamicMainBullets: 1,
                    formatFractionCurrent: e=>e,
                    formatFractionTotal: e=>e,
                    bulletClass: `${a}-bullet`,
                    bulletActiveClass: `${a}-bullet-active`,
                    modifierClass: `${a}-`,
                    currentClass: `${a}-current`,
                    totalClass: `${a}-total`,
                    hiddenClass: `${a}-hidden`,
                    progressbarFillClass: `${a}-progressbar-fill`,
                    progressbarOppositeClass: `${a}-progressbar-opposite`,
                    clickableClass: `${a}-clickable`,
                    lockClass: `${a}-lock`,
                    horizontalClass: `${a}-horizontal`,
                    verticalClass: `${a}-vertical`
                }
            }),
            e.pagination = {
                el: null,
                $el: null,
                bullets: []
            };
            let r = 0;
            function l() {
                return !e.params.pagination.el || !e.pagination.el || !e.pagination.$el || 0 === e.pagination.$el.length
            }
            function o(t, s) {
                const {bulletActiveClass: i} = e.params.pagination;
                t[s]().addClass(`${i}-${s}`)[s]().addClass(`${i}-${s}-${s}`)
            }
            function d() {
                const t = e.rtl
                  , s = e.params.pagination;
                if (l())
                    return;
                const a = e.virtual && e.params.virtual.enabled ? e.virtual.slides.length : e.slides.length
                  , d = e.pagination.$el;
                let p;
                const c = e.params.loop ? Math.ceil((a - 2 * e.loopedSlides) / e.params.slidesPerGroup) : e.snapGrid.length;
                if (e.params.loop ? (p = Math.ceil((e.activeIndex - e.loopedSlides) / e.params.slidesPerGroup),
                p > a - 1 - 2 * e.loopedSlides && (p -= a - 2 * e.loopedSlides),
                p > c - 1 && (p -= c),
                p < 0 && "bullets" !== e.params.paginationType && (p = c + p)) : p = void 0 !== e.snapIndex ? e.snapIndex : e.activeIndex || 0,
                "bullets" === s.type && e.pagination.bullets && e.pagination.bullets.length > 0) {
                    const i = e.pagination.bullets;
                    let a, l, c;
                    if (s.dynamicBullets && (n = i.eq(0)[e.isHorizontal() ? "outerWidth" : "outerHeight"](!0),
                    d.css(e.isHorizontal() ? "width" : "height", n * (s.dynamicMainBullets + 4) + "px"),
                    s.dynamicMainBullets > 1 && void 0 !== e.previousIndex && (r += p - (e.previousIndex - e.loopedSlides || 0),
                    r > s.dynamicMainBullets - 1 ? r = s.dynamicMainBullets - 1 : r < 0 && (r = 0)),
                    a = Math.max(p - r, 0),
                    l = a + (Math.min(i.length, s.dynamicMainBullets) - 1),
                    c = (l + a) / 2),
                    i.removeClass(["", "-next", "-next-next", "-prev", "-prev-prev", "-main"].map((e=>`${s.bulletActiveClass}${e}`)).join(" ")),
                    d.length > 1)
                        i.each((e=>{
                            const t = g(e)
                              , i = t.index();
                            i === p && t.addClass(s.bulletActiveClass),
                            s.dynamicBullets && (i >= a && i <= l && t.addClass(`${s.bulletActiveClass}-main`),
                            i === a && o(t, "prev"),
                            i === l && o(t, "next"))
                        }
                        ));
                    else {
                        const t = i.eq(p)
                          , n = t.index();
                        if (t.addClass(s.bulletActiveClass),
                        s.dynamicBullets) {
                            const t = i.eq(a)
                              , r = i.eq(l);
                            for (let e = a; e <= l; e += 1)
                                i.eq(e).addClass(`${s.bulletActiveClass}-main`);
                            if (e.params.loop)
                                if (n >= i.length) {
                                    for (let e = s.dynamicMainBullets; e >= 0; e -= 1)
                                        i.eq(i.length - e).addClass(`${s.bulletActiveClass}-main`);
                                    i.eq(i.length - s.dynamicMainBullets - 1).addClass(`${s.bulletActiveClass}-prev`)
                                } else
                                    o(t, "prev"),
                                    o(r, "next");
                            else
                                o(t, "prev"),
                                o(r, "next")
                        }
                    }
                    if (s.dynamicBullets) {
                        const a = Math.min(i.length, s.dynamicMainBullets + 4)
                          , r = (n * a - n) / 2 - c * n
                          , l = t ? "right" : "left";
                        i.css(e.isHorizontal() ? l : "top", `${r}px`)
                    }
                }
                if ("fraction" === s.type && (d.find(ee(s.currentClass)).text(s.formatFractionCurrent(p + 1)),
                d.find(ee(s.totalClass)).text(s.formatFractionTotal(c))),
                "progressbar" === s.type) {
                    let t;
                    t = s.progressbarOpposite ? e.isHorizontal() ? "vertical" : "horizontal" : e.isHorizontal() ? "horizontal" : "vertical";
                    const i = (p + 1) / c;
                    let a = 1
                      , n = 1;
                    "horizontal" === t ? a = i : n = i,
                    d.find(ee(s.progressbarFillClass)).transform(`translate3d(0,0,0) scaleX(${a}) scaleY(${n})`).transition(e.params.speed)
                }
                "custom" === s.type && s.renderCustom ? (d.html(s.renderCustom(e, p + 1, c)),
                i("paginationRender", d[0])) : i("paginationUpdate", d[0]),
                e.params.watchOverflow && e.enabled && d[e.isLocked ? "addClass" : "removeClass"](s.lockClass)
            }
            function p() {
                const t = e.params.pagination;
                if (l())
                    return;
                const s = e.virtual && e.params.virtual.enabled ? e.virtual.slides.length : e.slides.length
                  , a = e.pagination.$el;
                let n = "";
                if ("bullets" === t.type) {
                    let i = e.params.loop ? Math.ceil((s - 2 * e.loopedSlides) / e.params.slidesPerGroup) : e.snapGrid.length;
                    e.params.freeMode && e.params.freeMode.enabled && !e.params.loop && i > s && (i = s);
                    for (let s = 0; s < i; s += 1)
                        t.renderBullet ? n += t.renderBullet.call(e, s, t.bulletClass) : n += `<${t.bulletElement} class="${t.bulletClass}"></${t.bulletElement}>`;
                    a.html(n),
                    e.pagination.bullets = a.find(ee(t.bulletClass))
                }
                "fraction" === t.type && (n = t.renderFraction ? t.renderFraction.call(e, t.currentClass, t.totalClass) : `<span class="${t.currentClass}"></span> / <span class="${t.totalClass}"></span>`,
                a.html(n)),
                "progressbar" === t.type && (n = t.renderProgressbar ? t.renderProgressbar.call(e, t.progressbarFillClass) : `<span class="${t.progressbarFillClass}"></span>`,
                a.html(n)),
                "custom" !== t.type && i("paginationRender", e.pagination.$el[0])
            }
            function c() {
                e.params.pagination = Q(e, e.originalParams.pagination, e.params.pagination, {
                    el: "swiper-pagination"
                });
                const t = e.params.pagination;
                if (!t.el)
                    return;
                let s = g(t.el);
                0 !== s.length && (e.params.uniqueNavElements && "string" == typeof t.el && s.length > 1 && (s = e.$el.find(t.el),
                s.length > 1 && (s = s.filter((t=>g(t).parents(".swiper")[0] === e.el)))),
                "bullets" === t.type && t.clickable && s.addClass(t.clickableClass),
                s.addClass(t.modifierClass + t.type),
                s.addClass(t.modifierClass + e.params.direction),
                "bullets" === t.type && t.dynamicBullets && (s.addClass(`${t.modifierClass}${t.type}-dynamic`),
                r = 0,
                t.dynamicMainBullets < 1 && (t.dynamicMainBullets = 1)),
                "progressbar" === t.type && t.progressbarOpposite && s.addClass(t.progressbarOppositeClass),
                t.clickable && s.on("click", ee(t.bulletClass), (function(t) {
                    t.preventDefault();
                    let s = g(this).index() * e.params.slidesPerGroup;
                    e.params.loop && (s += e.loopedSlides),
                    e.slideTo(s)
                }
                )),
                Object.assign(e.pagination, {
                    $el: s,
                    el: s[0]
                }),
                e.enabled || s.addClass(t.lockClass))
            }
            function u() {
                const t = e.params.pagination;
                if (l())
                    return;
                const s = e.pagination.$el;
                s.removeClass(t.hiddenClass),
                s.removeClass(t.modifierClass + t.type),
                s.removeClass(t.modifierClass + e.params.direction),
                e.pagination.bullets && e.pagination.bullets.removeClass && e.pagination.bullets.removeClass(t.bulletActiveClass),
                t.clickable && s.off("click", ee(t.bulletClass))
            }
            s("init", (()=>{
                c(),
                p(),
                d()
            }
            )),
            s("activeIndexChange", (()=>{
                (e.params.loop || void 0 === e.snapIndex) && d()
            }
            )),
            s("snapIndexChange", (()=>{
                e.params.loop || d()
            }
            )),
            s("slidesLengthChange", (()=>{
                e.params.loop && (p(),
                d())
            }
            )),
            s("snapGridLengthChange", (()=>{
                e.params.loop || (p(),
                d())
            }
            )),
            s("destroy", (()=>{
                u()
            }
            )),
            s("enable disable", (()=>{
                const {$el: t} = e.pagination;
                t && t[e.enabled ? "removeClass" : "addClass"](e.params.pagination.lockClass)
            }
            )),
            s("lock unlock", (()=>{
                d()
            }
            )),
            s("click", ((t,s)=>{
                const a = s.target
                  , {$el: n} = e.pagination;
                if (e.params.pagination.el && e.params.pagination.hideOnClick && n.length > 0 && !g(a).hasClass(e.params.pagination.bulletClass)) {
                    if (e.navigation && (e.navigation.nextEl && a === e.navigation.nextEl || e.navigation.prevEl && a === e.navigation.prevEl))
                        return;
                    const t = n.hasClass(e.params.pagination.hiddenClass);
                    i(!0 === t ? "paginationShow" : "paginationHide"),
                    n.toggleClass(e.params.pagination.hiddenClass)
                }
            }
            )),
            Object.assign(e.pagination, {
                render: p,
                update: d,
                init: c,
                destroy: u
            })
        }
        function se({swiper: e, extendParams: t, on: s}) {
            t({
                parallax: {
                    enabled: !1
                }
            });
            const i = (t,s)=>{
                const {rtl: i} = e
                  , a = g(t)
                  , n = i ? -1 : 1
                  , r = a.attr("data-swiper-parallax") || "0";
                let l = a.attr("data-swiper-parallax-x")
                  , o = a.attr("data-swiper-parallax-y");
                const d = a.attr("data-swiper-parallax-scale")
                  , p = a.attr("data-swiper-parallax-opacity");
                if (l || o ? (l = l || "0",
                o = o || "0") : e.isHorizontal() ? (l = r,
                o = "0") : (o = r,
                l = "0"),
                l = l.indexOf("%") >= 0 ? parseInt(l, 10) * s * n + "%" : l * s * n + "px",
                o = o.indexOf("%") >= 0 ? parseInt(o, 10) * s + "%" : o * s + "px",
                null != p) {
                    const e = p - (p - 1) * (1 - Math.abs(s));
                    a[0].style.opacity = e
                }
                if (null == d)
                    a.transform(`translate3d(${l}, ${o}, 0px)`);
                else {
                    const e = d - (d - 1) * (1 - Math.abs(s));
                    a.transform(`translate3d(${l}, ${o}, 0px) scale(${e})`)
                }
            }
              , a = ()=>{
                const {$el: t, slides: s, progress: a, snapGrid: n} = e;
                t.children("[data-swiper-parallax], [data-swiper-parallax-x], [data-swiper-parallax-y], [data-swiper-parallax-opacity], [data-swiper-parallax-scale]").each((e=>{
                    i(e, a)
                }
                )),
                s.each(((t,s)=>{
                    let r = t.progress;
                    e.params.slidesPerGroup > 1 && "auto" !== e.params.slidesPerView && (r += Math.ceil(s / 2) - a * (n.length - 1)),
                    r = Math.min(Math.max(r, -1), 1),
                    g(t).find("[data-swiper-parallax], [data-swiper-parallax-x], [data-swiper-parallax-y], [data-swiper-parallax-opacity], [data-swiper-parallax-scale]").each((e=>{
                        i(e, r)
                    }
                    ))
                }
                ))
            }
            ;
            s("beforeInit", (()=>{
                e.params.parallax.enabled && (e.params.watchSlidesProgress = !0,
                e.originalParams.watchSlidesProgress = !0)
            }
            )),
            s("init", (()=>{
                e.params.parallax.enabled && a()
            }
            )),
            s("setTranslate", (()=>{
                e.params.parallax.enabled && a()
            }
            )),
            s("setTransition", ((t,s)=>{
                e.params.parallax.enabled && ((t=e.params.speed)=>{
                    const {$el: s} = e;
                    s.find("[data-swiper-parallax], [data-swiper-parallax-x], [data-swiper-parallax-y], [data-swiper-parallax-opacity], [data-swiper-parallax-scale]").each((e=>{
                        const s = g(e);
                        let i = parseInt(s.attr("data-swiper-parallax-duration"), 10) || t;
                        0 === t && (i = 0),
                        s.transition(i)
                    }
                    ))
                }
                )(s)
            }
            ))
        }
        function ie({swiper: e, extendParams: t, on: s, emit: i}) {
            t({
                lazy: {
                    checkInView: !1,
                    enabled: !1,
                    loadPrevNext: !1,
                    loadPrevNextAmount: 1,
                    loadOnTransitionStart: !1,
                    scrollingElement: "",
                    elementClass: "swiper-lazy",
                    loadingClass: "swiper-lazy-loading",
                    loadedClass: "swiper-lazy-loaded",
                    preloaderClass: "swiper-lazy-preloader"
                }
            }),
            e.lazy = {};
            let a = !1
              , n = !1;
            function r(t, s=!0) {
                const a = e.params.lazy;
                if (void 0 === t)
                    return;
                if (0 === e.slides.length)
                    return;
                const n = e.virtual && e.params.virtual.enabled ? e.$wrapperEl.children(`.${e.params.slideClass}[data-swiper-slide-index="${t}"]`) : e.slides.eq(t)
                  , l = n.find(`.${a.elementClass}:not(.${a.loadedClass}):not(.${a.loadingClass})`);
                !n.hasClass(a.elementClass) || n.hasClass(a.loadedClass) || n.hasClass(a.loadingClass) || l.push(n[0]),
                0 !== l.length && l.each((t=>{
                    const l = g(t);
                    l.addClass(a.loadingClass);
                    const o = l.attr("data-background")
                      , d = l.attr("data-src")
                      , p = l.attr("data-srcset")
                      , c = l.attr("data-sizes")
                      , u = l.parent("picture");
                    e.loadImage(l[0], d || o, p, c, !1, (()=>{
                        if (null != e && e && (!e || e.params) && !e.destroyed) {
                            if (o ? (l.css("background-image", `url("${o}")`),
                            l.removeAttr("data-background")) : (p && (l.attr("srcset", p),
                            l.removeAttr("data-srcset")),
                            c && (l.attr("sizes", c),
                            l.removeAttr("data-sizes")),
                            u.length && u.children("source").each((e=>{
                                const t = g(e);
                                t.attr("data-srcset") && (t.attr("srcset", t.attr("data-srcset")),
                                t.removeAttr("data-srcset"))
                            }
                            )),
                            d && (l.attr("src", d),
                            l.removeAttr("data-src"))),
                            l.addClass(a.loadedClass).removeClass(a.loadingClass),
                            n.find(`.${a.preloaderClass}`).remove(),
                            e.params.loop && s) {
                                const t = n.attr("data-swiper-slide-index");
                                n.hasClass(e.params.slideDuplicateClass) ? r(e.$wrapperEl.children(`[data-swiper-slide-index="${t}"]:not(.${e.params.slideDuplicateClass})`).index(), !1) : r(e.$wrapperEl.children(`.${e.params.slideDuplicateClass}[data-swiper-slide-index="${t}"]`).index(), !1)
                            }
                            i("lazyImageReady", n[0], l[0]),
                            e.params.autoHeight && e.updateAutoHeight()
                        }
                    }
                    )),
                    i("lazyImageLoad", n[0], l[0])
                }
                ))
            }
            function l() {
                const {$wrapperEl: t, params: s, slides: i, activeIndex: a} = e
                  , l = e.virtual && s.virtual.enabled
                  , o = s.lazy;
                let d = s.slidesPerView;
                function p(e) {
                    if (l) {
                        if (t.children(`.${s.slideClass}[data-swiper-slide-index="${e}"]`).length)
                            return !0
                    } else if (i[e])
                        return !0;
                    return !1
                }
                function c(e) {
                    return l ? g(e).attr("data-swiper-slide-index") : g(e).index()
                }
                if ("auto" === d && (d = 0),
                n || (n = !0),
                e.params.watchSlidesProgress)
                    t.children(`.${s.slideVisibleClass}`).each((e=>{
                        r(l ? g(e).attr("data-swiper-slide-index") : g(e).index())
                    }
                    ));
                else if (d > 1)
                    for (let e = a; e < a + d; e += 1)
                        p(e) && r(e);
                else
                    r(a);
                if (o.loadPrevNext)
                    if (d > 1 || o.loadPrevNextAmount && o.loadPrevNextAmount > 1) {
                        const e = o.loadPrevNextAmount
                          , t = d
                          , s = Math.min(a + t + Math.max(e, t), i.length)
                          , n = Math.max(a - Math.max(t, e), 0);
                        for (let e = a + d; e < s; e += 1)
                            p(e) && r(e);
                        for (let e = n; e < a; e += 1)
                            p(e) && r(e)
                    } else {
                        const e = t.children(`.${s.slideNextClass}`);
                        e.length > 0 && r(c(e));
                        const i = t.children(`.${s.slidePrevClass}`);
                        i.length > 0 && r(c(i))
                    }
            }
            function d() {
                const t = o();
                if (!e || e.destroyed)
                    return;
                const s = e.params.lazy.scrollingElement ? g(e.params.lazy.scrollingElement) : g(t)
                  , i = s[0] === t
                  , n = i ? t.innerWidth : s[0].offsetWidth
                  , r = i ? t.innerHeight : s[0].offsetHeight
                  , p = e.$el.offset()
                  , {rtlTranslate: c} = e;
                let u = !1;
                c && (p.left -= e.$el[0].scrollLeft);
                const h = [[p.left, p.top], [p.left + e.width, p.top], [p.left, p.top + e.height], [p.left + e.width, p.top + e.height]];
                for (let e = 0; e < h.length; e += 1) {
                    const t = h[e];
                    if (t[0] >= 0 && t[0] <= n && t[1] >= 0 && t[1] <= r) {
                        if (0 === t[0] && 0 === t[1])
                            continue;
                        u = !0
                    }
                }
                const f = !("touchstart" !== e.touchEvents.start || !e.support.passiveListener || !e.params.passiveListeners) && {
                    passive: !0,
                    capture: !1
                };
                u ? (l(),
                s.off("scroll", d, f)) : a || (a = !0,
                s.on("scroll", d, f))
            }
            s("beforeInit", (()=>{
                e.params.lazy.enabled && e.params.preloadImages && (e.params.preloadImages = !1)
            }
            )),
            s("init", (()=>{
                e.params.lazy.enabled && (e.params.lazy.checkInView ? d() : l())
            }
            )),
            s("scroll", (()=>{
                e.params.freeMode && e.params.freeMode.enabled && !e.params.freeMode.sticky && l()
            }
            )),
            s("scrollbarDragMove resize _freeModeNoMomentumRelease", (()=>{
                e.params.lazy.enabled && (e.params.lazy.checkInView ? d() : l())
            }
            )),
            s("transitionStart", (()=>{
                e.params.lazy.enabled && (e.params.lazy.loadOnTransitionStart || !e.params.lazy.loadOnTransitionStart && !n) && (e.params.lazy.checkInView ? d() : l())
            }
            )),
            s("transitionEnd", (()=>{
                e.params.lazy.enabled && !e.params.lazy.loadOnTransitionStart && (e.params.lazy.checkInView ? d() : l())
            }
            )),
            s("slideChange", (()=>{
                const {lazy: t, cssMode: s, watchSlidesProgress: i, touchReleaseOnEdges: a, resistanceRatio: n} = e.params;
                t.enabled && (s || i && (a || 0 === n)) && l()
            }
            )),
            Object.assign(e.lazy, {
                load: l,
                loadInSlide: r
            })
        }
        function ae({swiper: e, extendParams: t, on: s}) {
            function i(e, t) {
                const s = function() {
                    let e, t, s;
                    return (i,a)=>{
                        for (t = -1,
                        e = i.length; e - t > 1; )
                            s = e + t >> 1,
                            i[s] <= a ? t = s : e = s;
                        return e
                    }
                }();
                let i, a;
                return this.x = e,
                this.y = t,
                this.lastIndex = e.length - 1,
                this.interpolate = function(e) {
                    return e ? (a = s(this.x, e),
                    i = a - 1,
                    (e - this.x[i]) * (this.y[a] - this.y[i]) / (this.x[a] - this.x[i]) + this.y[i]) : 0
                }
                ,
                this
            }
            function a() {
                e.controller.control && e.controller.spline && (e.controller.spline = void 0,
                delete e.controller.spline)
            }
            t({
                controller: {
                    control: void 0,
                    inverse: !1,
                    by: "slide"
                }
            }),
            e.controller = {
                control: void 0
            },
            s("beforeInit", (()=>{
                e.controller.control = e.params.controller.control
            }
            )),
            s("update", (()=>{
                a()
            }
            )),
            s("resize", (()=>{
                a()
            }
            )),
            s("observerUpdate", (()=>{
                a()
            }
            )),
            s("setTranslate", ((t,s,i)=>{
                e.controller.control && e.controller.setTranslate(s, i)
            }
            )),
            s("setTransition", ((t,s,i)=>{
                e.controller.control && e.controller.setTransition(s, i)
            }
            )),
            Object.assign(e.controller, {
                setTranslate: function(t, s) {
                    const a = e.controller.control;
                    let n, r;
                    const l = e.constructor;
                    function o(t) {
                        const s = e.rtlTranslate ? -e.translate : e.translate;
                        "slide" === e.params.controller.by && (function(t) {
                            e.controller.spline || (e.controller.spline = e.params.loop ? new i(e.slidesGrid,t.slidesGrid) : new i(e.snapGrid,t.snapGrid))
                        }(t),
                        r = -e.controller.spline.interpolate(-s)),
                        r && "container" !== e.params.controller.by || (n = (t.maxTranslate() - t.minTranslate()) / (e.maxTranslate() - e.minTranslate()),
                        r = (s - e.minTranslate()) * n + t.minTranslate()),
                        e.params.controller.inverse && (r = t.maxTranslate() - r),
                        t.updateProgress(r),
                        t.setTranslate(r, e),
                        t.updateActiveIndex(),
                        t.updateSlidesClasses()
                    }
                    if (Array.isArray(a))
                        for (let e = 0; e < a.length; e += 1)
                            a[e] !== s && a[e]instanceof l && o(a[e]);
                    else
                        a instanceof l && s !== a && o(a)
                },
                setTransition: function(t, s) {
                    const i = e.constructor
                      , a = e.controller.control;
                    let n;
                    function r(s) {
                        s.setTransition(t, e),
                        0 !== t && (s.transitionStart(),
                        s.params.autoHeight && v((()=>{
                            s.updateAutoHeight()
                        }
                        )),
                        s.$wrapperEl.transitionEnd((()=>{
                            a && (s.params.loop && "slide" === e.params.controller.by && s.loopFix(),
                            s.transitionEnd())
                        }
                        )))
                    }
                    if (Array.isArray(a))
                        for (n = 0; n < a.length; n += 1)
                            a[n] !== s && a[n]instanceof i && r(a[n]);
                    else
                        a instanceof i && s !== a && r(a)
                }
            })
        }
        function ne({swiper: e, extendParams: t, on: s}) {
            t({
                a11y: {
                    enabled: !0,
                    notificationClass: "swiper-notification",
                    prevSlideMessage: "Previous slide",
                    nextSlideMessage: "Next slide",
                    firstSlideMessage: "This is the first slide",
                    lastSlideMessage: "This is the last slide",
                    paginationBulletMessage: "Go to slide {{index}}",
                    slideLabelMessage: "{{index}} / {{slidesLength}}",
                    containerMessage: null,
                    containerRoleDescriptionMessage: null,
                    itemRoleDescriptionMessage: null,
                    slideRole: "group"
                }
            });
            let i = null;
            function a(e) {
                const t = i;
                0 !== t.length && (t.html(""),
                t.html(e))
            }
            function n(e) {
                e.attr("tabIndex", "0")
            }
            function r(e) {
                e.attr("tabIndex", "-1")
            }
            function l(e, t) {
                e.attr("role", t)
            }
            function o(e, t) {
                e.attr("aria-roledescription", t)
            }
            function d(e, t) {
                e.attr("aria-label", t)
            }
            function p(e) {
                e.attr("aria-disabled", !0)
            }
            function c(e) {
                e.attr("aria-disabled", !1)
            }
            function u(t) {
                if (13 !== t.keyCode && 32 !== t.keyCode)
                    return;
                const s = e.params.a11y
                  , i = g(t.target);
                e.navigation && e.navigation.$nextEl && i.is(e.navigation.$nextEl) && (e.isEnd && !e.params.loop || e.slideNext(),
                e.isEnd ? a(s.lastSlideMessage) : a(s.nextSlideMessage)),
                e.navigation && e.navigation.$prevEl && i.is(e.navigation.$prevEl) && (e.isBeginning && !e.params.loop || e.slidePrev(),
                e.isBeginning ? a(s.firstSlideMessage) : a(s.prevSlideMessage)),
                e.pagination && i.is(ee(e.params.pagination.bulletClass)) && i[0].click()
            }
            function h() {
                if (e.params.loop || e.params.rewind || !e.navigation)
                    return;
                const {$nextEl: t, $prevEl: s} = e.navigation;
                s && s.length > 0 && (e.isBeginning ? (p(s),
                r(s)) : (c(s),
                n(s))),
                t && t.length > 0 && (e.isEnd ? (p(t),
                r(t)) : (c(t),
                n(t)))
            }
            function f() {
                return e.pagination && e.pagination.bullets && e.pagination.bullets.length
            }
            function m() {
                return f() && e.params.pagination.clickable
            }
            const v = (e,t,s)=>{
                n(e),
                "BUTTON" !== e[0].tagName && (l(e, "button"),
                e.on("keydown", u)),
                d(e, s),
                function(e, t) {
                    e.attr("aria-controls", t)
                }(e, t)
            }
            ;
            s("beforeInit", (()=>{
                i = g(`<span class="${e.params.a11y.notificationClass}" aria-live="assertive" aria-atomic="true"></span>`)
            }
            )),
            s("afterInit", (()=>{
                e.params.a11y.enabled && (function() {
                    const t = e.params.a11y;
                    e.$el.append(i);
                    const s = e.$el;
                    t.containerRoleDescriptionMessage && o(s, t.containerRoleDescriptionMessage),
                    t.containerMessage && d(s, t.containerMessage);
                    const a = e.$wrapperEl
                      , n = a.attr("id") || `swiper-wrapper-${function(e=16) {
                        return "x".repeat(e).replace(/x/g, (()=>Math.round(16 * Math.random()).toString(16)))
                    }(16)}`
                      , r = e.params.autoplay && e.params.autoplay.enabled ? "off" : "polite";
                    var p;
                    p = n,
                    a.attr("id", p),
                    function(e, t) {
                        e.attr("aria-live", t)
                    }(a, r),
                    t.itemRoleDescriptionMessage && o(g(e.slides), t.itemRoleDescriptionMessage),
                    l(g(e.slides), t.slideRole);
                    const c = e.params.loop ? e.slides.filter((t=>!t.classList.contains(e.params.slideDuplicateClass))).length : e.slides.length;
                    let h, f;
                    e.slides.each(((s,i)=>{
                        const a = g(s)
                          , n = e.params.loop ? parseInt(a.attr("data-swiper-slide-index"), 10) : i;
                        d(a, t.slideLabelMessage.replace(/\{\{index\}\}/, n + 1).replace(/\{\{slidesLength\}\}/, c))
                    }
                    )),
                    e.navigation && e.navigation.$nextEl && (h = e.navigation.$nextEl),
                    e.navigation && e.navigation.$prevEl && (f = e.navigation.$prevEl),
                    h && h.length && v(h, n, t.nextSlideMessage),
                    f && f.length && v(f, n, t.prevSlideMessage),
                    m() && e.pagination.$el.on("keydown", ee(e.params.pagination.bulletClass), u)
                }(),
                h())
            }
            )),
            s("toEdge", (()=>{
                e.params.a11y.enabled && h()
            }
            )),
            s("fromEdge", (()=>{
                e.params.a11y.enabled && h()
            }
            )),
            s("paginationUpdate", (()=>{
                e.params.a11y.enabled && function() {
                    const t = e.params.a11y;
                    f() && e.pagination.bullets.each((s=>{
                        const i = g(s);
                        e.params.pagination.clickable && (n(i),
                        e.params.pagination.renderBullet || (l(i, "button"),
                        d(i, t.paginationBulletMessage.replace(/\{\{index\}\}/, i.index() + 1)))),
                        i.is(`.${e.params.pagination.bulletActiveClass}`) ? i.attr("aria-current", "true") : i.removeAttr("aria-current")
                    }
                    ))
                }()
            }
            )),
            s("destroy", (()=>{
                e.params.a11y.enabled && function() {
                    let t, s;
                    i && i.length > 0 && i.remove(),
                    e.navigation && e.navigation.$nextEl && (t = e.navigation.$nextEl),
                    e.navigation && e.navigation.$prevEl && (s = e.navigation.$prevEl),
                    t && t.off("keydown", u),
                    s && s.off("keydown", u),
                    m() && e.pagination.$el.off("keydown", ee(e.params.pagination.bulletClass), u)
                }()
            }
            ))
        }
        function re({swiper: e, extendParams: t, on: s, emit: i}) {
            let a;
            function n() {
                const t = e.slides.eq(e.activeIndex);
                let s = e.params.autoplay.delay;
                t.attr("data-swiper-autoplay") && (s = t.attr("data-swiper-autoplay") || e.params.autoplay.delay),
                clearTimeout(a),
                a = v((()=>{
                    let t;
                    e.params.autoplay.reverseDirection ? e.params.loop ? (e.loopFix(),
                    t = e.slidePrev(e.params.speed, !0, !0),
                    i("autoplay")) : e.isBeginning ? e.params.autoplay.stopOnLastSlide ? o() : (t = e.slideTo(e.slides.length - 1, e.params.speed, !0, !0),
                    i("autoplay")) : (t = e.slidePrev(e.params.speed, !0, !0),
                    i("autoplay")) : e.params.loop ? (e.loopFix(),
                    t = e.slideNext(e.params.speed, !0, !0),
                    i("autoplay")) : e.isEnd ? e.params.autoplay.stopOnLastSlide ? o() : (t = e.slideTo(0, e.params.speed, !0, !0),
                    i("autoplay")) : (t = e.slideNext(e.params.speed, !0, !0),
                    i("autoplay")),
                    (e.params.cssMode && e.autoplay.running || !1 === t) && n()
                }
                ), s)
            }
            function l() {
                return void 0 === a && !e.autoplay.running && (e.autoplay.running = !0,
                i("autoplayStart"),
                n(),
                !0)
            }
            function o() {
                return !!e.autoplay.running && void 0 !== a && (a && (clearTimeout(a),
                a = void 0),
                e.autoplay.running = !1,
                i("autoplayStop"),
                !0)
            }
            function d(t) {
                e.autoplay.running && (e.autoplay.paused || (a && clearTimeout(a),
                e.autoplay.paused = !0,
                0 !== t && e.params.autoplay.waitForTransition ? ["transitionend", "webkitTransitionEnd"].forEach((t=>{
                    e.$wrapperEl[0].addEventListener(t, c)
                }
                )) : (e.autoplay.paused = !1,
                n())))
            }
            function p() {
                const t = r();
                "hidden" === t.visibilityState && e.autoplay.running && d(),
                "visible" === t.visibilityState && e.autoplay.paused && (n(),
                e.autoplay.paused = !1)
            }
            function c(t) {
                e && !e.destroyed && e.$wrapperEl && t.target === e.$wrapperEl[0] && (["transitionend", "webkitTransitionEnd"].forEach((t=>{
                    e.$wrapperEl[0].removeEventListener(t, c)
                }
                )),
                e.autoplay.paused = !1,
                e.autoplay.running ? n() : o())
            }
            function u() {
                e.params.autoplay.disableOnInteraction ? o() : d(),
                ["transitionend", "webkitTransitionEnd"].forEach((t=>{
                    e.$wrapperEl[0].removeEventListener(t, c)
                }
                ))
            }
            function h() {
                e.params.autoplay.disableOnInteraction || (e.autoplay.paused = !1,
                n())
            }
            e.autoplay = {
                running: !1,
                paused: !1
            },
            t({
                autoplay: {
                    enabled: !1,
                    delay: 3e3,
                    waitForTransition: !0,
                    disableOnInteraction: !0,
                    stopOnLastSlide: !1,
                    reverseDirection: !1,
                    pauseOnMouseEnter: !1
                }
            }),
            s("init", (()=>{
                e.params.autoplay.enabled && (l(),
                r().addEventListener("visibilitychange", p),
                e.params.autoplay.pauseOnMouseEnter && (e.$el.on("mouseenter", u),
                e.$el.on("mouseleave", h)))
            }
            )),
            s("beforeTransitionStart", ((t,s,i)=>{
                e.autoplay.running && (i || !e.params.autoplay.disableOnInteraction ? e.autoplay.pause(s) : o())
            }
            )),
            s("sliderFirstMove", (()=>{
                e.autoplay.running && (e.params.autoplay.disableOnInteraction ? o() : d())
            }
            )),
            s("touchEnd", (()=>{
                e.params.cssMode && e.autoplay.paused && !e.params.autoplay.disableOnInteraction && n()
            }
            )),
            s("destroy", (()=>{
                e.$el.off("mouseenter", u),
                e.$el.off("mouseleave", h),
                e.autoplay.running && o(),
                r().removeEventListener("visibilitychange", p)
            }
            )),
            Object.assign(e.autoplay, {
                pause: d,
                run: n,
                start: l,
                stop: o
            })
        }
        s(8730),
        s(9307),
        s(6801)
    }
}]);
