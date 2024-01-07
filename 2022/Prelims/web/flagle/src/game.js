const FLAG = "gg{flagle_is_life}"

this.wordle = this.wordle || {}, this.wordle.bundle = function(e) {
    "use strict";

    function a(e) {
        return (a = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
            return typeof e
        } : function(e) {
            return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
        })(e)
    }

    function s(e, a) {
        if (!(e instanceof a)) throw new TypeError("Cannot call a class as a function")
    }

    function t(e, a) {
        for (var s = 0; s < a.length; s++) {
            var t = a[s];
            t.enumerable = t.enumerable || !1, t.configurable = !0, "value" in t && (t.writable = !0), Object.defineProperty(e, t.key, t)
        }
    }

    function n(e, a, s) {
        return a && t(e.prototype, a), s && t(e, s), e
    }

    function o(e, a, s) {
        return a in e ? Object.defineProperty(e, a, {
            value: s,
            enumerable: !0,
            configurable: !0,
            writable: !0
        }) : e[a] = s, e
    }

    function r(e, a) {
        if ("function" != typeof a && null !== a) throw new TypeError("Super expression must either be null or a function");
        e.prototype = Object.create(a && a.prototype, {
            constructor: {
                value: e,
                writable: !0,
                configurable: !0
            }
        }), a && l(e, a)
    }

    function i(e) {
        return (i = Object.setPrototypeOf ? Object.getPrototypeOf : function(e) {
            return e.__proto__ || Object.getPrototypeOf(e)
        })(e)
    }

    function l(e, a) {
        return (l = Object.setPrototypeOf || function(e, a) {
            return e.__proto__ = a, e
        })(e, a)
    }

    function d() {
        if ("undefined" == typeof Reflect || !Reflect.construct) return !1;
        if (Reflect.construct.sham) return !1;
        if ("function" == typeof Proxy) return !0;
        try {
            return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], (function() {}))), !0
        } catch (e) {
            return !1
        }
    }

    function c(e, a, s) {
        return (c = d() ? Reflect.construct : function(e, a, s) {
            var t = [null];
            t.push.apply(t, a);
            var n = new(Function.bind.apply(e, t));
            return s && l(n, s.prototype), n
        }).apply(null, arguments)
    }

    function u(e) {
        var a = "function" == typeof Map ? new Map : void 0;
        return (u = function(e) {
            if (null === e || (s = e, -1 === Function.toString.call(s).indexOf("[native code]"))) return e;
            var s;
            if ("function" != typeof e) throw new TypeError("Super expression must either be null or a function");
            if (void 0 !== a) {
                if (a.has(e)) return a.get(e);
                a.set(e, t)
            }

            function t() {
                return c(e, arguments, i(this).constructor)
            }
            return t.prototype = Object.create(e.prototype, {
                constructor: {
                    value: t,
                    enumerable: !1,
                    writable: !0,
                    configurable: !0
                }
            }), l(t, e)
        })(e)
    }

    function m(e) {
        if (void 0 === e) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
        return e
    }

    function p(e, a) {
        return !a || "object" != typeof a && "function" != typeof a ? m(e) : a
    }

    function h(e) {
        var a = d();
        return function() {
            var s, t = i(e);
            if (a) {
                var n = i(this).constructor;
                s = Reflect.construct(t, arguments, n)
            } else s = t.apply(this, arguments);
            return p(this, s)
        }
    }

    function y(e, a) {
        return function(e) {
            if (Array.isArray(e)) return e
        }(e) || function(e, a) {
            var s = null == e ? null : "undefined" != typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
            if (null == s) return;
            var t, n, o = [],
                r = !0,
                i = !1;
            try {
                for (s = s.call(e); !(r = (t = s.next()).done) && (o.push(t.value), !a || o.length !== a); r = !0);
            } catch (e) {
                i = !0, n = e
            } finally {
                try {
                    r || null == s.return || s.return()
                } finally {
                    if (i) throw n
                }
            }
            return o
        }(e, a) || b(e, a) || function() {
            throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
        }()
    }

    function g(e) {
        return function(e) {
            if (Array.isArray(e)) return f(e)
        }(e) || function(e) {
            if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"]) return Array.from(e)
        }(e) || b(e) || function() {
            throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
        }()
    }

    function b(e, a) {
        if (e) {
            if ("string" == typeof e) return f(e, a);
            var s = Object.prototype.toString.call(e).slice(8, -1);
            return "Object" === s && e.constructor && (s = e.constructor.name), "Map" === s || "Set" === s ? Array.from(e) : "Arguments" === s || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(s) ? f(e, a) : void 0
        }
    }

    function f(e, a) {
        (null == a || a > e.length) && (a = e.length);
        for (var s = 0, t = new Array(a); s < a; s++) t[s] = e[s];
        return t
    }
    var k = document.createElement("template");
    k.innerHTML = "\n<style>\n  :host {\n    display: inline-block;\n  }\n  .tile {\n    width: 100%;\n    display: inline-flex;\n    justify-content: center;\n    align-items: center;\n    font-size: 2rem;\n    line-height: 2rem;\n    font-weight: bold;\n    vertical-align: middle;\n    box-sizing: border-box;\n    color: var(--tile-text-color);\n    text-transform: uppercase;\n    user-select: none;\n  }\n  .tile::before {\n    content: '';\n    display: inline-block;\n    padding-bottom: 100%;\n  }\n\n  /* Allow tiles to be smaller on small screens */\n  @media (max-height: 600px) {\n    .tile {\n      font-size: 1em;\n      line-height: 1em;\n    }\n  }\n\n  .tile[data-state='empty'] {\n    border: 2px solid var(--color-tone-4);\n  }\n  .tile[data-state='tbd'] {\n    background-color: var(--color-tone-7);\n    border: 2px solid var(--color-tone-3);\n    color: var(--color-tone-1);\n  }\n  .tile[data-state='correct'] {\n    background-color: var(--color-correct);\n  }\n  .tile[data-state='present'] {\n    background-color: var(--color-present);\n  }\n  .tile[data-state='absent'] {\n    background-color: var(--color-absent);\n  }\n\n  .tile[data-animation='pop'] {\n    animation-name: PopIn;\n    animation-duration: 100ms;\n  }\n\n  @keyframes PopIn {\n    from {\n      transform: scale(0.8);\n      opacity: 0;\n    }\n\n    40% {\n      transform: scale(1.1);\n      opacity: 1;\n    }\n  }\n  .tile[data-animation='flip-in'] {\n    animation-name: FlipIn;\n    animation-duration: 250ms;\n    animation-timing-function: ease-in;\n  }\n  @keyframes FlipIn {\n    0% {\n      transform: rotateX(0);\n    }\n    100% {\n      transform: rotateX(-90deg);\n    }\n  }\n  .tile[data-animation='flip-out'] {\n    animation-name: FlipOut;\n    animation-duration: 250ms;\n    animation-timing-function: ease-in;\n  }\n  @keyframes FlipOut {\n    0% {\n      transform: rotateX(-90deg);\n    }\n    100% {\n      transform: rotateX(0);\n    }\n  }\n</style>\n<div class=\"tile\" data-state=\"empty\" data-animation=\"idle\"></div>\n";
    var v = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), o(m(e = a.call(this)), "_letter", ""), o(m(e), "_state", "empty"), o(m(e), "_animation", "idle"), o(m(e), "_last", !1), o(m(e), "_reveal", !1), e.attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "last",
            set: function(e) {
                this._last = e
            }
        }, {
            key: "connectedCallback",
            value: function() {
                var e = this;
                this.shadowRoot.appendChild(k.content.cloneNode(!0)), this.$tile = this.shadowRoot.querySelector(".tile"), this.$tile.addEventListener("animationend", (function(a) {
                    "PopIn" === a.animationName && (e._animation = "idle"), "FlipIn" === a.animationName && (e.$tile.dataset.state = e._state, e._animation = "flip-out"), "FlipOut" === a.animationName && (e._animation = "idle", e._last && e.dispatchEvent(new CustomEvent("game-last-tile-revealed-in-row", {
                        bubbles: !0,
                        composed: !0
                    }))), e._render()
                })), this._render()
            }
        }, {
            key: "attributeChangedCallback",
            value: function(e, a, s) {
                switch (e) {
                    case "letter":
                        if (s === a) break;
                        var t = "null" === s ? "" : s;
                        this._letter = t, this._state = t ? "tbd" : "empty", this._animation = t ? "pop" : "idle";
                        break;
                    case "evaluation":
                        if (!s) break;
                        this._state = s;
                        break;
                    case "reveal":
                        this._animation = "flip-in", this._reveal = !0
                }
                this._render()
            }
        }, {
            key: "_render",
            value: function() {
                this.$tile && (this.$tile.textContent = this._letter, ["empty", "tbd"].includes(this._state) && (this.$tile.dataset.state = this._state), (["empty", "tbd"].includes(this._state) || this._reveal) && this.$tile.dataset.animation != this._animation && (this.$tile.dataset.animation = this._animation))
            }
        }], [{
            key: "observedAttributes",
            get: function() {
                return ["letter", "evaluation", "reveal"]
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("game-tile", v);
    var w = document.createElement("template");
    w.innerHTML = `\n  <style>\n    :host {\n      display: block;\n    }\n    :host([invalid]){\n      animation-name: Shake;\n      animation-duration: 600ms;\n    }\n    .row {\n      display: grid;\n      grid-template-columns: repeat(${FLAG.length}, 1fr);\n      grid-gap: 5px;\n    }\n    .win {\n      animation-name: Bounce;\n      animation-duration: 1000ms;\n    }\n\n    @keyframes Bounce {\n      0%, 20% {\n        transform: translateY(0);\n      }\n      40% {\n        transform: translateY(-30px);\n      }\n      50% {\n        transform: translateY(5px);\n      }\n      60% {\n        transform: translateY(-15px);\n      }\n      80% {\n        transform: translateY(2px);\n      }\n      100% {\n        transform: translateY(0);\n      }\n    }\n\n    @keyframes Shake {\n      10%,\n      90% {\n        transform: translateX(-1px);\n      }\n\n      20%,\n      80% {\n        transform: translateX(2px);\n      }\n\n      30%,\n      50%,\n      70% {\n        transform: translateX(-4px);\n      }\n\n      40%,\n      60% {\n        transform: translateX(4px);\n      }\n    }\n  </style>\n  <div class="row"></div>\n`;
    var x = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), (e = a.call(this)).attachShadow({
                mode: "open"
            }), e._letters = "", e._evaluation = [], e._length, e
        }
        return n(t, [{
            key: "evaluation",
            get: function() {
                return this._evaluation
            },
            set: function(e) {
                var a = this;
                this._evaluation = e, this.$tiles && this.$tiles.forEach((function(e, s) {
                    e.setAttribute("evaluation", a._evaluation[s]), setTimeout((function() {
                        e.setAttribute("reveal", "")
                    }), 300 * s)
                }))
            }
        }, {
            key: "connectedCallback",
            value: function() {
                var e = this;
                this.shadowRoot.appendChild(w.content.cloneNode(!0)), this.$row = this.shadowRoot.querySelector(".row");
                for (var a = function(a) {
                        var s = document.createElement("game-tile"),
                            t = e._letters[a];
                        (t && s.setAttribute("letter", t), e._evaluation[a]) && (s.setAttribute("evaluation", e._evaluation[a]), setTimeout((function() {
                            s.setAttribute("reveal", "")
                        }), 100 * a));
                        a === e._length - 1 && (s.last = !0), e.$row.appendChild(s)
                    }, s = 0; s < this._length; s++) a(s);
                this.$tiles = this.shadowRoot.querySelectorAll("game-tile"), this.addEventListener("animationend", (function(a) {
                    "Shake" === a.animationName && e.removeAttribute("invalid")
                }))
            }
        }, {
            key: "attributeChangedCallback",
            value: function(e, a, s) {
                switch (e) {
                    case "letters":
                        this._letters = s || "";
                        break;
                    case "length":
                        this._length = parseInt(s, 10);
                        break;
                    case "win":
                        if (null === s) {
                            this.$tiles.forEach((function(e) {
                                e.classList.remove("win")
                            }));
                            break
                        }
                        this.$tiles.forEach((function(e, a) {
                            e.classList.add("win"), e.style.animationDelay = "".concat(100 * a, "ms")
                        }))
                }
                this._render()
            }
        }, {
            key: "_render",
            value: function() {
                var e = this;
                this.$row && this.$tiles.forEach((function(a, s) {
                    var t = e._letters[s];
                    t ? a.setAttribute("letter", t) : a.removeAttribute("letter")
                }))
            }
        }], [{
            key: "observedAttributes",
            get: function() {
                return ["letters", "length", "invalid", "win"]
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("game-row", x);
    var z = document.createElement("template");
    z.innerHTML = "\n  <slot></slot>\n";
    var j = "nyt-wordle-darkmode",
        S = "nyt-wordle-cbmode",
        C = function(e) {
            r(t, e);
            var a = h(t);

            function t() {
                var e;
                s(this, t), o(m(e = a.call(this)), "isDarkTheme", !1), o(m(e), "isColorBlindTheme", !1), e.attachShadow({
                    mode: "open"
                });
                var n = JSON.parse(window.localStorage.getItem(j)),
                    r = window.matchMedia("(prefers-color-scheme: dark)").matches,
                    i = JSON.parse(window.localStorage.getItem(S));
                return !0 === n || !1 === n ? e.setDarkTheme(n) : r && e.setDarkTheme(!0), !0 !== i && !1 !== i || e.setColorBlindTheme(i), window.themeManager = m(e), e
            }
            return n(t, [{
                key: "setDarkTheme",
                value: function(e) {
                    var a = document.querySelector("body");
                    e && !a.classList.contains("nightmode") ? a.classList.add("nightmode") : a.classList.remove("nightmode"), this.isDarkTheme = e, window.localStorage.setItem(j, JSON.stringify(e))
                }
            }, {
                key: "setColorBlindTheme",
                value: function(e) {
                    var a = document.querySelector("body");
                    e && !a.classList.contains("colorblind") ? a.classList.add("colorblind") : a.classList.remove("colorblind"), this.isColorBlindTheme = e, window.localStorage.setItem(S, JSON.stringify(e))
                }
            }, {
                key: "connectedCallback",
                value: function() {
                    var e = this;
                    this.shadowRoot.appendChild(z.content.cloneNode(!0)), this.shadowRoot.addEventListener("game-setting-change", (function(a) {
                        var s = a.detail,
                            t = s.name,
                            n = s.checked;
                        switch (t) {
                            case "dark-theme":
                                return void e.setDarkTheme(n);
                            case "color-blind-theme":
                                return void e.setColorBlindTheme(n)
                        }
                    }))
                }
            }]), t
        }(u(HTMLElement));

    function E(e, a) {
        return e === a || e != e && a != a
    }

    function _(e, a) {
        for (var s = e.length; s--;)
            if (E(e[s][0], a)) return s;
        return -1
    }
    customElements.define("game-theme-manager", C);
    var q = Array.prototype.splice;

    function L(e) {
        var a = -1,
            s = null == e ? 0 : e.length;
        for (this.clear(); ++a < s;) {
            var t = e[a];
            this.set(t[0], t[1])
        }
    }
    L.prototype.clear = function() {
        this.__data__ = [], this.size = 0
    }, L.prototype.delete = function(e) {
        var a = this.__data__,
            s = _(a, e);
        return !(s < 0) && (s == a.length - 1 ? a.pop() : q.call(a, s, 1), --this.size, !0)
    }, L.prototype.get = function(e) {
        var a = this.__data__,
            s = _(a, e);
        return s < 0 ? void 0 : a[s][1]
    }, L.prototype.has = function(e) {
        return _(this.__data__, e) > -1
    }, L.prototype.set = function(e, a) {
        var s = this.__data__,
            t = _(s, e);
        return t < 0 ? (++this.size, s.push([e, a])) : s[t][1] = a, this
    };
    var T = "object" == ("undefined" == typeof global ? "undefined" : a(global)) && global && global.Object === Object && global,
        A = "object" == ("undefined" == typeof self ? "undefined" : a(self)) && self && self.Object === Object && self,
        I = T || A || Function("return this")(),
        M = I.Symbol,
        O = Object.prototype,
        R = O.hasOwnProperty,
        H = O.toString,
        N = M ? M.toStringTag : void 0;
    var P = Object.prototype.toString;
    var $ = M ? M.toStringTag : void 0;

    function D(e) {
        return null == e ? void 0 === e ? "[object Undefined]" : "[object Null]" : $ && $ in Object(e) ? function(e) {
            var a = R.call(e, N),
                s = e[N];
            try {
                e[N] = void 0;
                var t = !0
            } catch (e) {}
            var n = H.call(e);
            return t && (a ? e[N] = s : delete e[N]), n
        }(e) : function(e) {
            return P.call(e)
        }(e)
    }

    function B(e) {
        var s = a(e);
        return null != e && ("object" == s || "function" == s)
    }

    function G(e) {
        if (!B(e)) return !1;
        var a = D(e);
        return "[object Function]" == a || "[object GeneratorFunction]" == a || "[object AsyncFunction]" == a || "[object Proxy]" == a
    }
    var V, F = I["__core-js_shared__"],
        W = (V = /[^.]+$/.exec(F && F.keys && F.keys.IE_PROTO || "")) ? "Symbol(src)_1." + V : "";
    var Y = Function.prototype.toString;
    var U = /^\[object .+?Constructor\]$/,
        J = Function.prototype,
        X = Object.prototype,
        Z = J.toString,
        K = X.hasOwnProperty,
        Q = RegExp("^" + Z.call(K).replace(/[\\^$.*+?()[\]{}|]/g, "\\$&").replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g, "$1.*?") + "$");

    function ee(e) {
        return !(!B(e) || (a = e, W && W in a)) && (G(e) ? Q : U).test(function(e) {
            if (null != e) {
                try {
                    return Y.call(e)
                } catch (e) {}
                try {
                    return e + ""
                } catch (e) {}
            }
            return ""
        }(e));
        var a
    }

    function ae(e, a) {
        var s = function(e, a) {
            return null == e ? void 0 : e[a]
        }(e, a);
        return ee(s) ? s : void 0
    }
    var se = ae(I, "Map"),
        te = ae(Object, "create");
    var ne = Object.prototype.hasOwnProperty;
    var oe = Object.prototype.hasOwnProperty;

    function re(e) {
        var a = -1,
            s = null == e ? 0 : e.length;
        for (this.clear(); ++a < s;) {
            var t = e[a];
            this.set(t[0], t[1])
        }
    }

    function ie(e, s) {
        var t, n, o = e.__data__;
        return ("string" == (n = a(t = s)) || "number" == n || "symbol" == n || "boolean" == n ? "__proto__" !== t : null === t) ? o["string" == typeof s ? "string" : "hash"] : o.map
    }

    function le(e) {
        var a = -1,
            s = null == e ? 0 : e.length;
        for (this.clear(); ++a < s;) {
            var t = e[a];
            this.set(t[0], t[1])
        }
    }
    re.prototype.clear = function() {
        this.__data__ = te ? te(null) : {}, this.size = 0
    }, re.prototype.delete = function(e) {
        var a = this.has(e) && delete this.__data__[e];
        return this.size -= a ? 1 : 0, a
    }, re.prototype.get = function(e) {
        var a = this.__data__;
        if (te) {
            var s = a[e];
            return "__lodash_hash_undefined__" === s ? void 0 : s
        }
        return ne.call(a, e) ? a[e] : void 0
    }, re.prototype.has = function(e) {
        var a = this.__data__;
        return te ? void 0 !== a[e] : oe.call(a, e)
    }, re.prototype.set = function(e, a) {
        var s = this.__data__;
        return this.size += this.has(e) ? 0 : 1, s[e] = te && void 0 === a ? "__lodash_hash_undefined__" : a, this
    }, le.prototype.clear = function() {
        this.size = 0, this.__data__ = {
            hash: new re,
            map: new(se || L),
            string: new re
        }
    }, le.prototype.delete = function(e) {
        var a = ie(this, e).delete(e);
        return this.size -= a ? 1 : 0, a
    }, le.prototype.get = function(e) {
        return ie(this, e).get(e)
    }, le.prototype.has = function(e) {
        return ie(this, e).has(e)
    }, le.prototype.set = function(e, a) {
        var s = ie(this, e),
            t = s.size;
        return s.set(e, a), this.size += s.size == t ? 0 : 1, this
    };

    function de(e) {
        var a = this.__data__ = new L(e);
        this.size = a.size
    }
    de.prototype.clear = function() {
        this.__data__ = new L, this.size = 0
    }, de.prototype.delete = function(e) {
        var a = this.__data__,
            s = a.delete(e);
        return this.size = a.size, s
    }, de.prototype.get = function(e) {
        return this.__data__.get(e)
    }, de.prototype.has = function(e) {
        return this.__data__.has(e)
    }, de.prototype.set = function(e, a) {
        var s = this.__data__;
        if (s instanceof L) {
            var t = s.__data__;
            if (!se || t.length < 199) return t.push([e, a]), this.size = ++s.size, this;
            s = this.__data__ = new le(t)
        }
        return s.set(e, a), this.size = s.size, this
    };
    var ce = function() {
        try {
            var e = ae(Object, "defineProperty");
            return e({}, "", {}), e
        } catch (e) {}
    }();

    function ue(e, a, s) {
        "__proto__" == a && ce ? ce(e, a, {
            configurable: !0,
            enumerable: !0,
            value: s,
            writable: !0
        }) : e[a] = s
    }

    function me(e, a, s) {
        (void 0 !== s && !E(e[a], s) || void 0 === s && !(a in e)) && ue(e, a, s)
    }
    var pe, he = function(e, a, s) {
            for (var t = -1, n = Object(e), o = s(e), r = o.length; r--;) {
                var i = o[pe ? r : ++t];
                if (!1 === a(n[i], i, n)) break
            }
            return e
        },
        ye = "object" == (void 0 === e ? "undefined" : a(e)) && e && !e.nodeType && e,
        ge = ye && "object" == ("undefined" == typeof module ? "undefined" : a(module)) && module && !module.nodeType && module,
        be = ge && ge.exports === ye ? I.Buffer : void 0,
        fe = be ? be.allocUnsafe : void 0;
    var ke = I.Uint8Array;

    function ve(e, a) {
        var s, t, n = a ? (s = e.buffer, t = new s.constructor(s.byteLength), new ke(t).set(new ke(s)), t) : e.buffer;
        return new e.constructor(n, e.byteOffset, e.length)
    }
    var we = Object.create,
        xe = function() {
            function e() {}
            return function(a) {
                if (!B(a)) return {};
                if (we) return we(a);
                e.prototype = a;
                var s = new e;
                return e.prototype = void 0, s
            }
        }();
    var ze, je, Se = (ze = Object.getPrototypeOf, je = Object, function(e) {
            return ze(je(e))
        }),
        Ce = Object.prototype;

    function Ee(e) {
        var a = e && e.constructor;
        return e === ("function" == typeof a && a.prototype || Ce)
    }

    function _e(e) {
        return null != e && "object" == a(e)
    }

    function qe(e) {
        return _e(e) && "[object Arguments]" == D(e)
    }
    var Le = Object.prototype,
        Te = Le.hasOwnProperty,
        Ae = Le.propertyIsEnumerable,
        Ie = qe(function() {
            return arguments
        }()) ? qe : function(e) {
            return _e(e) && Te.call(e, "callee") && !Ae.call(e, "callee")
        },
        Me = Array.isArray;

    function Oe(e) {
        return "number" == typeof e && e > -1 && e % 1 == 0 && e <= 9007199254740991
    }

    function Re(e) {
        return null != e && Oe(e.length) && !G(e)
    }
    var He = "object" == (void 0 === e ? "undefined" : a(e)) && e && !e.nodeType && e,
        Ne = He && "object" == ("undefined" == typeof module ? "undefined" : a(module)) && module && !module.nodeType && module,
        Pe = Ne && Ne.exports === He ? I.Buffer : void 0,
        $e = (Pe ? Pe.isBuffer : void 0) || function() {
            return !1
        },
        De = Function.prototype,
        Be = Object.prototype,
        Ge = De.toString,
        Ve = Be.hasOwnProperty,
        Fe = Ge.call(Object);
    var We = {};
    We["[object Float32Array]"] = We["[object Float64Array]"] = We["[object Int8Array]"] = We["[object Int16Array]"] = We["[object Int32Array]"] = We["[object Uint8Array]"] = We["[object Uint8ClampedArray]"] = We["[object Uint16Array]"] = We["[object Uint32Array]"] = !0, We["[object Arguments]"] = We["[object Array]"] = We["[object ArrayBuffer]"] = We["[object Boolean]"] = We["[object DataView]"] = We["[object Date]"] = We["[object Error]"] = We["[object Function]"] = We["[object Map]"] = We["[object Number]"] = We["[object Object]"] = We["[object RegExp]"] = We["[object Set]"] = We["[object String]"] = We["[object WeakMap]"] = !1;
    var Ye = "object" == (void 0 === e ? "undefined" : a(e)) && e && !e.nodeType && e,
        Ue = Ye && "object" == ("undefined" == typeof module ? "undefined" : a(module)) && module && !module.nodeType && module,
        Je = Ue && Ue.exports === Ye && T.process,
        Xe = function() {
            try {
                var e = Ue && Ue.require && Ue.require("util").types;
                return e || Je && Je.binding && Je.binding("util")
            } catch (e) {}
        }(),
        Ze = Xe && Xe.isTypedArray,
        Ke = Ze ? function(e) {
            return function(a) {
                return e(a)
            }
        }(Ze) : function(e) {
            return _e(e) && Oe(e.length) && !!We[D(e)]
        };

    function Qe(e, a) {
        if (("constructor" !== a || "function" != typeof e[a]) && "__proto__" != a) return e[a]
    }
    var ea = Object.prototype.hasOwnProperty;

    function aa(e, a, s) {
        var t = e[a];
        ea.call(e, a) && E(t, s) && (void 0 !== s || a in e) || ue(e, a, s)
    }
    var sa = /^(?:0|[1-9]\d*)$/;

    function ta(e, s) {
        var t = a(e);
        return !!(s = null == s ? 9007199254740991 : s) && ("number" == t || "symbol" != t && sa.test(e)) && e > -1 && e % 1 == 0 && e < s
    }
    var na = Object.prototype.hasOwnProperty;

    function oa(e, a) {
        var s = Me(e),
            t = !s && Ie(e),
            n = !s && !t && $e(e),
            o = !s && !t && !n && Ke(e),
            r = s || t || n || o,
            i = r ? function(e, a) {
                for (var s = -1, t = Array(e); ++s < e;) t[s] = a(s);
                return t
            }(e.length, String) : [],
            l = i.length;
        for (var d in e) !a && !na.call(e, d) || r && ("length" == d || n && ("offset" == d || "parent" == d) || o && ("buffer" == d || "byteLength" == d || "byteOffset" == d) || ta(d, l)) || i.push(d);
        return i
    }
    var ra = Object.prototype.hasOwnProperty;

    function ia(e) {
        if (!B(e)) return function(e) {
            var a = [];
            if (null != e)
                for (var s in Object(e)) a.push(s);
            return a
        }(e);
        var a = Ee(e),
            s = [];
        for (var t in e)("constructor" != t || !a && ra.call(e, t)) && s.push(t);
        return s
    }

    function la(e) {
        return Re(e) ? oa(e, !0) : ia(e)
    }

    function da(e) {
        return function(e, a, s, t) {
            var n = !s;
            s || (s = {});
            for (var o = -1, r = a.length; ++o < r;) {
                var i = a[o],
                    l = t ? t(s[i], e[i], i, s, e) : void 0;
                void 0 === l && (l = e[i]), n ? ue(s, i, l) : aa(s, i, l)
            }
            return s
        }(e, la(e))
    }

    function ca(e, a, s, t, n, o, r) {
        var i = Qe(e, s),
            l = Qe(a, s),
            d = r.get(l);
        if (d) me(e, s, d);
        else {
            var c, u = o ? o(i, l, s + "", e, a, r) : void 0,
                m = void 0 === u;
            if (m) {
                var p = Me(l),
                    h = !p && $e(l),
                    y = !p && !h && Ke(l);
                u = l, p || h || y ? Me(i) ? u = i : _e(c = i) && Re(c) ? u = function(e, a) {
                    var s = -1,
                        t = e.length;
                    for (a || (a = Array(t)); ++s < t;) a[s] = e[s];
                    return a
                }(i) : h ? (m = !1, u = function(e, a) {
                    if (a) return e.slice();
                    var s = e.length,
                        t = fe ? fe(s) : new e.constructor(s);
                    return e.copy(t), t
                }(l, !0)) : y ? (m = !1, u = ve(l, !0)) : u = [] : function(e) {
                    if (!_e(e) || "[object Object]" != D(e)) return !1;
                    var a = Se(e);
                    if (null === a) return !0;
                    var s = Ve.call(a, "constructor") && a.constructor;
                    return "function" == typeof s && s instanceof s && Ge.call(s) == Fe
                }(l) || Ie(l) ? (u = i, Ie(i) ? u = da(i) : B(i) && !G(i) || (u = function(e) {
                    return "function" != typeof e.constructor || Ee(e) ? {} : xe(Se(e))
                }(l))) : m = !1
            }
            m && (r.set(l, u), n(u, l, t, o, r), r.delete(l)), me(e, s, u)
        }
    }

    function ua(e, a, s, t, n) {
        e !== a && he(a, (function(o, r) {
            if (n || (n = new de), B(o)) ca(e, a, r, s, ua, t, n);
            else {
                var i = t ? t(Qe(e, r), o, r + "", e, a, n) : void 0;
                void 0 === i && (i = o), me(e, r, i)
            }
        }), la)
    }

    function ma(e) {
        return e
    }

    function pa(e, a, s) {
        switch (s.length) {
            case 0:
                return e.call(a);
            case 1:
                return e.call(a, s[0]);
            case 2:
                return e.call(a, s[0], s[1]);
            case 3:
                return e.call(a, s[0], s[1], s[2])
        }
        return e.apply(a, s)
    }
    var ha = Math.max;
    var ya = ce ? function(e, a) {
            return ce(e, "toString", {
                configurable: !0,
                enumerable: !1,
                value: (s = a, function() {
                    return s
                }),
                writable: !0
            });
            var s
        } : ma,
        ga = Date.now;
    var ba = function(e) {
        var a = 0,
            s = 0;
        return function() {
            var t = ga(),
                n = 16 - (t - s);
            if (s = t, n > 0) {
                if (++a >= 800) return arguments[0]
            } else a = 0;
            return e.apply(void 0, arguments)
        }
    }(ya);

    function fa(e, a) {
        return ba(function(e, a, s) {
            return a = ha(void 0 === a ? e.length - 1 : a, 0),
                function() {
                    for (var t = arguments, n = -1, o = ha(t.length - a, 0), r = Array(o); ++n < o;) r[n] = t[a + n];
                    n = -1;
                    for (var i = Array(a + 1); ++n < a;) i[n] = t[n];
                    return i[a] = s(r), pa(e, this, i)
                }
        }(e, a, ma), e + "")
    }
    var ka, va = (ka = function(e, a, s) {
            ua(e, a, s)
        }, fa((function(e, s) {
            var t = -1,
                n = s.length,
                o = n > 1 ? s[n - 1] : void 0,
                r = n > 2 ? s[2] : void 0;
            for (o = ka.length > 3 && "function" == typeof o ? (n--, o) : void 0, r && function(e, s, t) {
                    if (!B(t)) return !1;
                    var n = a(s);
                    return !!("number" == n ? Re(t) && ta(s, t.length) : "string" == n && s in t) && E(t[s], e)
                }(s[0], s[1], r) && (o = n < 3 ? void 0 : o, n = 1), e = Object(e); ++t < n;) {
                var i = s[t];
                i && ka(e, i, t, o)
            }
            return e
        }))),
        wa = "nyt-wordle-state",
        xa = {
            boardState: null,
            evaluations: null,
            rowIndex: null,
            solution: null,
            gameStatus: null,
            lastPlayedTs: null,
            lastCompletedTs: null,
            restoringFromLocalStorage: null,
            hardMode: !1
        };

    function za() {
        var e = window.localStorage.getItem(wa) || JSON.stringify(xa);
        return JSON.parse(e)
    }

    function ja(e) {
        var a = za();
        ! function(e) {
            window.localStorage.setItem(wa, JSON.stringify(e))
        }(va(a, e))
    }

    function Sa() {
        var e = navigator.userAgent || navigator.vendor || window.opera;
        return /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(e) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(e.substr(0, 4))
    }

    function Ca() {
        var e = navigator.userAgent;
        return e.match(/chrome|chromium|crios/i) ? "chrome" : e.match(/firefox|fxios/i) ? "firefox" : e.match(/safari/i) ? "safari" : e.match(/opr\//i) ? "opera" : e.match(/edg/i) ? "edge" : "No browser detection"
    }
    var Ea = "mailto:nytgames@nytimes.com";

    function _a(e) {
        return e.charAt(0).toUpperCase() + e.slice(1)
    }
    var qa = function(e) {
            var a = [];
            return Object.keys(e).forEach((function(s) {
                a.push("".concat(encodeURIComponent(s), "=").concat(encodeURIComponent(e[s])))
            })), "?".concat(a.join("&"))
        },
        La = document.createElement("template");
    La.innerHTML = '\n  <style>\n  .setting {\n    display: flex;\n    justify-content: space-between;\n    align-items: center;\n    border-bottom: 1px solid var(--color-tone-4);\n    padding: 16px 0;\n  }\n\n  a, a:visited {\n    color: var(--color-tone-2);\n  }\n\n  .title {\n    font-size: 18px;\n  }\n  .text {\n    padding-right: 8px;\n  }\n  .description {\n    font-size: 12px;\n    color: var(--color-tone-2);\n  }\n\n  #footnote {\n    position: absolute;\n    bottom: 0;\n    left: 0;\n    right: 0;\n    padding: 16px;\n    color: var(--color-tone-2);\n    font-size: 12px;\n    text-align: right;\n    display: flex;\n    justify-content: space-between;\n    align-items: flex-end;\n  }\n\n  @media only screen and (min-device-width : 320px) and (max-device-width : 480px) {\n    .setting {\n      padding: 16px;\n    }\n  }\n\n  </style>\n  <div class="sections">\n    <section>\n      <div class="setting">\n        <div class="text">\n          <div class="title">Hard Mode</div>\n          <div class="description">Any revealed hints must be used in subsequent guesses</div>\n        </div>\n        <div class="control">\n          <game-switch id="hard-mode" name="hard-mode"></game-switch>\n        </div>\n      </div>\n      <div class="setting">\n        <div class="text">\n          <div class="title">Dark Theme</div>\n        </div>\n        <div class="control">\n          <game-switch id="dark-theme" name="dark-theme"></game-switch>\n        </div>\n      </div>\n      <div class="setting">\n        <div class="text">\n          <div class="title">High Contrast Mode</div>\n          <div class="description">For improved color vision</div>\n        </div>\n        <div class="control">\n          <game-switch id="color-blind-theme" name="color-blind-theme"></game-switch>\n        </div>\n      </div>\n    </section>\n\n    <section>\n      <div class="setting">\n        <div class="text">\n          <div class="title">Feedback</div>\n        </div>\n        <div class="control">\n          <a href="'.concat(function() {
        var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "Flagle Feedback",
            a = (new Date).getTimezoneOffset(),
            s = "\r\n\r\n\n--\nDevice summary:\nPage: /games/wordle\nPlatform: ".concat(Sa() ? "Web (Mobile)" : "Web (Desktop)", " \nBrowser: ").concat(_a(Ca()), "\nScreen Resolution: ").concat(window.screen.width, " x ").concat(window.screen.height, "\nViewport Size: ").concat(document.documentElement.clientWidth, " x ").concat(document.documentElement.clientHeight, "\nTimezone: ", "UTC".concat(a > 0 ? "" : "+").concat(a / -60), "\n  ");
        return Ea + qa({
            subject: e,
            body: s
        })
    }(), '" title="nytgames@nytimes.com">Email</a>\n        </div>\n      </div>\n      <div class="setting">\n        <div class="text">\n          <div class="title">Community</div>\n        </div>\n        <div class="control">\n          <a href="https://twitter.com/NYTimesWordplay" target="blank" title="@NYTimesWordplay">Twitter</a>\n        </div>\n      </div>\n      <div class="setting">\n      <div class="text">\n        <div class="title">Questions?</div>\n      </div>\n      <div class="control">\n        <a href="https://help.nytimes.com/hc/en-us/articles/360029050872-Word-Games-and-Logic-Puzzles#h_01FVGCB2Z00ZQMDMCYWBPWJNXB" target="blank">FAQ</a>\n      </div>\n    </div>\n    </section>\n  </div>\n  <div id="footnote">\n    <div id="copyright">&#169; ').concat((new Date).getFullYear(), ' The New York Times Company</div>\n    <div>\n      <div id="puzzle-number"></div>\n      <div id="hash"></div>\n    </div>\n  </div>\n');
    var Ta = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), o(m(e = a.call(this)), "gameApp", void 0), e.attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "connectedCallback",
            value: function() {
                var e, a = this;
                this.shadowRoot.appendChild(La.content.cloneNode(!0)), this.shadowRoot.querySelector("#hash").textContent = null === (e = window.wordle) || void 0 === e ? void 0 : e.hash, this.shadowRoot.querySelector("#puzzle-number").textContent = "#".concat(this.gameApp.dayOffset), this.shadowRoot.addEventListener("game-switch-change", (function(e) {
                    e.stopPropagation();
                    var s = e.detail,
                        t = s.name,
                        n = s.checked,
                        o = s.disabled;
                    a.dispatchEvent(new CustomEvent("game-setting-change", {
                        bubbles: !0,
                        composed: !0,
                        detail: {
                            name: t,
                            checked: n,
                            disabled: o
                        }
                    })), a.render()
                })), this.render()
            }
        }, {
            key: "render",
            value: function() {
                var e = document.querySelector("body");
                e.classList.contains("nightmode") && this.shadowRoot.querySelector("#dark-theme").setAttribute("checked", ""), e.classList.contains("colorblind") && this.shadowRoot.querySelector("#color-blind-theme").setAttribute("checked", "");
                var a = za();
                a.hardMode && this.shadowRoot.querySelector("#hard-mode").setAttribute("checked", ""), a.hardMode || "IN_PROGRESS" !== a.gameStatus || 0 === a.rowIndex || (this.shadowRoot.querySelector("#hard-mode").removeAttribute("checked"), this.shadowRoot.querySelector("#hard-mode").setAttribute("disabled", ""))
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("game-settings", Ta);
    var Aa = document.createElement("template");
    Aa.innerHTML = '\n  <style>\n    .toast {\n      position: relative;\n      margin: 16px;\n      background-color: var(--color-tone-1);\n      color: var(--color-tone-7);\n      padding: 16px;\n      border: none;\n      border-radius: 4px;\n      opacity: 1;\n      transition: opacity 300ms cubic-bezier(0.645, 0.045, 0.355, 1);\n      font-weight: 700;\n    }\n    .win {\n      background-color: var(--color-correct);\n      color: var(--tile-text-color);\n    }\n    .fade {\n      opacity: 0;\n    }\n  </style>\n  <div class="toast"></div>\n';
    var Ia = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), o(m(e = a.call(this)), "_duration", void 0), e.attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "connectedCallback",
            value: function() {
                var e = this;
                this.shadowRoot.appendChild(Aa.content.cloneNode(!0));
                var a = this.shadowRoot.querySelector(".toast");
                a.textContent = this.getAttribute("text"), this._duration = this.getAttribute("duration") || 1e3, "Infinity" !== this._duration && setTimeout((function() {
                    a.classList.add("fade")
                }), this._duration), a.addEventListener("transitionend", (function(a) {
                    e.parentNode.removeChild(e)
                }))
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("game-toast", Ia);
    var Ra = "present",
        Ha = "correct",
        Na = "absent";
    var Pa = {
        unknown: 0,
        absent: 1,
        present: 2,
        correct: 3
    };

    function $a(e, a) {
        var s = {};
        return e.forEach((function(e, t) {
            if (a[t])
                for (var n = 0; n < e.length; n++) {
                    var o = e[n],
                        r = a[t][n],
                        i = s[o] || "unknown";
                    Pa[r] > Pa[i] && (s[o] = r)
                }
        })), s
    }

    function Da(e) {
        var a = ["th", "st", "nd", "rd"],
            s = e % 100;
        return e + (a[(s - 20) % 10] || a[s] || a[0])
    }
    var Ba = new Date(2021, 5, 19, 0, 0, 0, 0);

    function Ga(e, a) {
        var s = new Date(e),
            t = new Date(a).setHours(0, 0, 0, 0) - s.setHours(0, 0, 0, 0);
        return Math.round(t / 864e5)
    }

    function Fa(e) {
        return Ga(Ba, e)
    }
    var Wa = "abcdefghijklmnopqrstuvwxyz0123456789{}_";
    var Ya = "nyt-wordle-statistics",
        Ua = "fail",
        Ja = {
            currentStreak: 0,
            maxStreak: 0,
            guesses: o({
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0
            }, Ua, 0),
            winPercentage: 0,
            gamesPlayed: 0,
            gamesWon: 0,
            averageGuesses: 0
        };

    function Xa() {
        var e = window.localStorage.getItem(Ya) || JSON.stringify(Ja);
        return JSON.parse(e)
    }

    function Za(e) {
        var a = e.isWin,
            s = e.isStreak,
            t = e.numGuesses,
            n = Xa();
        window.willFixStreak && (1 === n.currentStreak && n.currentStreak < n.maxStreak && (n.currentStreak += n.maxStreak, n.maxStreak += 1), window.willFixStreak = !1), a ? (n.guesses[t] += 1, s ? n.currentStreak += 1 : n.currentStreak = 1) : (n.currentStreak = 0, n.guesses.fail += 1), n.maxStreak = Math.max(n.currentStreak, n.maxStreak), n.gamesPlayed += 1, n.gamesWon += a ? 1 : 0, n.winPercentage = Math.round(n.gamesWon / n.gamesPlayed * 100), n.averageGuesses = Math.round(Object.entries(n.guesses).reduce((function(e, a) {
                var s = y(a, 2),
                    t = s[0],
                    n = s[1];
                return t !== Ua ? e += t * n : e
            }), 0) / n.gamesWon),
            function(e) {
                window.localStorage.setItem(Ya, JSON.stringify(e))
            }(n)
    }
    var Ka, Qa = "nyt-wordle-refresh",
        es = window.localStorage;

    function as() {
        return Ka || (Ka = setInterval((function() {
            es.getItem(Qa) && (es.removeItem(Qa), window.location.href.match(/.*\.nytimes\.com/g) ? window.location.reload(!0) : window.location.replace("https://www.nytimes.com/games/wordle"))
        }), 432e5))
    }
    var ss = "nyt-wordle-statistics",
        ts = window.localStorage;

    function ns(e, a) {
        if (!e.gamesPlayed) return !1;
        var s = function() {
            var e = {
                gamesPlayed: 0
            };
            try {
                var a = JSON.parse(ts.getItem(ss));
                if (a && a.gamesPlayed) return a
            } catch (a) {
                return e
            }
            return e
        }();
        return !(s.gamesPlayed && !a) || e.gamesPlayed > s.gamesPlayed
    }

    function os() {
        if (ts) {
            try {
                var e = new Proxy(new URLSearchParams(window.location.search), {
                    get: function(e, a) {
                        return e.get(a)
                    }
                });
                if (e.data) ! function(e) {
                    if (!e.statistics) throw new Error("User local data does not contain statistics. Aborting transfer.");
                    if (ns(e.statistics, e.force)) {
                        ts.setItem(ss, JSON.stringify(e.statistics));
                        var a = e.darkTheme;
                        window.themeManager.setDarkTheme(a);
                        var s = !!e.colorBlindTheme;
                        window.themeManager.setColorBlindTheme(s)
                    }
                }(JSON.parse(e.data))
            } catch (e) {}
            window.history.replaceState({}, document.title, new URL(location.pathname, location.href).href)
        }
    }
    var rs = document.createElement("template");
    rs.innerHTML = "\n  <style>\n  .toaster {\n    position: absolute;\n    top: 10%;\n    left: 50%;\n    transform: translate(-50%, 0);\n    pointer-events: none;\n    width: fit-content;\n  }\n  #game-toaster {\n    z-index: ".concat(1e3, ";\n  }\n  #system-toaster {\n    z-index: ").concat(4e3, ';\n  }\n\n  #game {\n    width: 100%;\n    max-width: var(--game-max-width);\n    margin: 0 auto;\n    height: calc(100% - var(--header-height));\n    display: flex;\n    flex-direction: column;\n  }\n  header {\n    display: flex;\n    flex-direction: row;\n    align-items: center;\n    justify-content: space-between;\n    flex-wrap: nowrap;\n    padding: 0 16px;\n    height: var(--header-height);\n    color: var(--color-tone-1);\n    border-bottom: 1px solid var(--color-tone-4);\n  }\n  header .title {\n    font-family: \'nyt-karnakcondensed\';\n    font-weight: 700;\n    font-size: 37px;\n    line-height: 100%;\n    letter-spacing: 0.01em;\n    text-align: center;\n    left: 0;\n    right: 0;\n    pointer-events: none;\n  }\n  menu-left {\n    display: flex;\n    margin: 0;\n    padding: 0;\n    list-style: none;\n    align-items: center;\n  }\n  menu-right {\n    display: inline-block;\n  }\n  #nav-button {\n    padding-top: 2px;\n  }\n\n  @media (min-width: 415px) {\n    header {\n      padding: 0px 16px;\n    }\n  }\n\n  @media (max-width: 360px) {\n    header .title {\n      font-size: 22px;\n      letter-spacing: 0.1rem;\n    }\n  }\n\n  #board-container {\n    display: flex;\n    justify-content: center;\n    align-items: center;\n    flex-grow: 1;\n    overflow: hidden;\n  }\n  #board {\n    display: grid;\n    grid-template-rows: repeat(6, 1fr);\n    grid-gap: 5px;\n    padding:10px;\n    box-sizing: border-box;\n  }\n  button.icon {\n    background: none;\n    border: none;\n    cursor: pointer;\n    padding: 0 4px;\n  }\n\n  #debug-tools {\n    position: absolute;\n    bottom: 0;\n  }\n\n  </style>\n  <game-theme-manager>\n  <header>\n  <div class="menu-left" style="display: flex;">\n    <button id="nav-button" class="icon" aria-label="Navigation menu. Click for links to other NYT Games and our Privacy Policy." tabindex="-1">\n      <nav-icon></nav-icon>\n    </button>\n    <button id="help-button" class="icon" aria-label="Help" tabindex="-1">\n      <game-icon icon="help"></game-icon>\n    </button>\n  </div>\n  <div class="title">\n    Flagle\n  </div>\n  <div class="menu-right">\n    <button id="statistics-button" class="icon" aria-label="Statistics" tabindex="-1">\n      <game-icon icon="statistics"></game-icon>\n    </button>\n    <button id="settings-button" class="icon" aria-label="Settings" tabindex="-1">\n      <game-icon icon="settings"></game-icon>\n    </button>\n  </div>\n</header>\n    <div id="game">\n        <div id="board-container">\n          <div id="board"></div>\n        </div>\n        <game-keyboard></game-keyboard>\n        <game-nav-modal></game-nav-modal>\n        <game-modal></game-modal>\n        <game-page></game-page>\n        <div class="toaster" id="game-toaster"></div>\n        <div class="toaster" id="system-toaster"></div>\n    </div>\n  </game-theme-manager>\n  <div id="debug-tools"></div>\n');
    var is = document.createElement("template");
    is.innerHTML = '\n<button id="reveal">reveal</button>\n<button id="shake">shake</button>\n<button id="bounce">bounce</button>\n<button id="toast">toast</button>\n<button id="modal">modal</button>\n';
    var ls = "IN_PROGRESS",
        ds = "WIN",
        cs = "FAIL",
        us = ["Genius", "Magnificent", "Impressive", "Splendid", "Great", "Phew"],
        ms = function(e) {
            r(t, e);
            var a = h(t);

            function t() {
                var e;
                s(this, t), o(m(e = a.call(this)), "tileIndex", 0), o(m(e), "rowIndex", 0), o(m(e), "solution", void 0), o(m(e), "boardState", void 0), o(m(e), "evaluations", void 0), o(m(e), "canInput", !0), o(m(e), "gameStatus", ls), o(m(e), "letterEvaluations", {}), o(m(e), "$board", void 0), o(m(e), "$keyboard", void 0), o(m(e), "$game", void 0), o(m(e), "today", void 0), o(m(e), "lastPlayedTs", void 0), o(m(e), "lastCompletedTs", void 0), o(m(e), "hardMode", void 0), o(m(e), "dayOffset", void 0), e.attachShadow({
                    mode: "open"
                }), e.today = new Date, e.refreshTimer = as();
                var n = za();
                e.lastPlayedTs = n.lastPlayedTs, e.lastCompletedTs = n.lastCompletedTs;
                var r = new Date("02/10/2022 19:00:00 EST");
                return window.willFixStreak = !!e.lastCompletedTs && new Date(e.lastCompletedTs) < new Date(r), !e.lastPlayedTs || Ga(new Date(e.lastPlayedTs), e.today) >= 1 ? (e.boardState = new Array(6).fill(""), e.evaluations = new Array(6).fill(null), e.solution = FLAG, e.dayOffset = Fa(e.today), e.lastCompletedTs = n.lastCompletedTs, e.hardMode = n.hardMode, e.restoringFromLocalStorage = !1, ja({
                    rowIndex: e.rowIndex,
                    boardState: e.boardState,
                    evaluations: e.evaluations,
                    solution: e.solution,
                    gameStatus: e.gameStatus
                })) : (e.boardState = n.boardState, e.evaluations = n.evaluations, e.rowIndex = n.rowIndex, e.solution = n.solution, e.dayOffset = Fa(e.today), e.letterEvaluations = $a(e.boardState, e.evaluations), e.gameStatus = n.gameStatus, e.lastCompletedTs = n.lastCompletedTs, e.hardMode = n.hardMode, e.gameStatus !== ls && (e.canInput = !1), e.restoringFromLocalStorage = !0), e
            }
            return n(t, [{
                key: "evaluateRow",
                value: function() {
                    if (FLAG.length === this.tileIndex && !(this.rowIndex >= 6)) {
                        var e, a = this.$board.querySelectorAll("game-row")[this.rowIndex],
                            s = this.boardState[this.rowIndex];
                        if (this.hardMode) {
                            var t = function(e, a, s) {
                                    if (!e || !a || !s) return {
                                        validGuess: !0
                                    };
                                    for (var t = 0; t < s.length; t++)
                                        if (s[t] === Ha && e[t] !== a[t]) return {
                                            validGuess: !1,
                                            errorMessage: "".concat(Da(t + 1), " letter must be ").concat(a[t].toUpperCase())
                                        };
                                    for (var n = {}, o = 0; o < s.length; o++)[Ha, Ra].includes(s[o]) && (n[a[o]] ? n[a[o]] += 1 : n[a[o]] = 1);
                                    var r = e.split("").reduce((function(e, a) {
                                        return e[a] ? e[a] += 1 : e[a] = 1, e
                                    }), {});
                                    for (var i in n)
                                        if ((r[i] || 0) < n[i]) return {
                                            validGuess: !1,
                                            errorMessage: "Guess must contain ".concat(i.toUpperCase())
                                        };
                                    return {
                                        validGuess: !0
                                    }
                                }(s, this.boardState[this.rowIndex - 1], this.evaluations[this.rowIndex - 1]),
                                n = t.validGuess,
                                o = t.errorMessage;
                            if (!n) return a.setAttribute("invalid", ""), void this.addToast(o || "Not valid in hard mode")
                        }
                        var r = function(e, a) {
                            for (var s = Array(a.length).fill(Na), t = Array(a.length).fill(!0), n = Array(a.length).fill(!0), o = 0; o < e.length; o++) e[o] === a[o] && n[o] && (s[o] = Ha, t[o] = !1, n[o] = !1);
                            for (var r = 0; r < e.length; r++) {
                                var i = e[r];
                                if (t[r])
                                    for (var l = 0; l < a.length; l++) {
                                        var d = a[l];
                                        if (n[l] && i === d) {
                                            s[r] = Ra, n[l] = !1;
                                            break
                                        }
                                    }
                            }
                            return s
                        }(s, this.solution);
                        this.evaluations[this.rowIndex] = r, this.letterEvaluations = $a(this.boardState, this.evaluations), a.evaluation = this.evaluations[this.rowIndex], this.rowIndex += 1;
                        var i = this.rowIndex >= 6,
                            l = r.every((function(e) {
                                return "correct" === e
                            }));
                        if (i || l) {
                            Za({
                                isWin: l,
                                isStreak: !0,
                                numGuesses: this.rowIndex
                            }), ja({
                                lastCompletedTs: Date.now()
                            }), this.gameStatus = l ? ds : cs, es.setItem(Qa, !0)
                        }
                        this.tileIndex = 0, this.canInput = !1, ja({
                            rowIndex: this.rowIndex,
                            boardState: this.boardState,
                            evaluations: this.evaluations,
                            solution: this.solution,
                            gameStatus: this.gameStatus,
                            lastPlayedTs: Date.now()
                        })
                    }
                }
            }, {
                key: "addLetter",
                value: function(e) {
                    this.gameStatus === ls && (this.canInput && (this.tileIndex >= FLAG.length || (this.boardState[this.rowIndex] += e, this.$board.querySelectorAll("game-row")[this.rowIndex].setAttribute("letters", this.boardState[this.rowIndex]), this.tileIndex += 1)))
                }
            }, {
                key: "removeLetter",
                value: function() {
                    if (this.gameStatus === ls && this.canInput && !(this.tileIndex <= 0)) {
                        this.boardState[this.rowIndex] = this.boardState[this.rowIndex].slice(0, this.boardState[this.rowIndex].length - 1);
                        var e = this.$board.querySelectorAll("game-row")[this.rowIndex];
                        this.boardState[this.rowIndex] ? e.setAttribute("letters", this.boardState[this.rowIndex]) : e.removeAttribute("letters"), e.removeAttribute("invalid"), this.tileIndex -= 1
                    }
                }
            }, {
                key: "submitGuess",
                value: function() {
                    if (this.gameStatus === ls && this.canInput) {
                        if (FLAG.length !== this.tileIndex) return this.$board.querySelectorAll("game-row")[this.rowIndex].setAttribute("invalid", ""), void this.addToast("Not enough letters");
                        this.evaluateRow()
                    }
                }
            }, {
                key: "addToast",
                value: function(e, a) {
                    var s = arguments.length > 2 && void 0 !== arguments[2] && arguments[2],
                        t = document.createElement("game-toast");
                    t.setAttribute("text", e), a && t.setAttribute("duration", a), s ? this.shadowRoot.querySelector("#system-toaster").prepend(t) : this.shadowRoot.querySelector("#game-toaster").prepend(t)
                }
            }, {
                key: "sizeBoard",
                value: function() {
                    var e = this.shadowRoot.querySelector("#board-container"),
                        a = Math.min(Math.floor(e.clientHeight * (FLAG.length / 6)), 900),
                        s = 6 * Math.floor(a / FLAG.length);
                    this.$board.style.width = "".concat(a, "px"), this.$board.style.height = "".concat(s, "px")
                }
            }, {
                key: "showStatsModal",
                value: function() {
                    var e = this.$game.querySelector("game-modal"),
                        a = document.createElement("game-stats");
                    this.gameStatus === ds && this.rowIndex <= 6 && a.setAttribute("highlight-guess", this.rowIndex), a.gameApp = this, e.appendChild(a), e.setAttribute("open", "")
                }
            }, {
                key: "showNavModal",
                value: function() {
                    var e = this.$game.querySelector("game-nav-modal"),
                        a = document.createElement("game-nav");
                    a.gameApp = this, e.appendChild(a), e.setAttribute("open", "")
                }
            }, {
                key: "showHelpModal",
                value: function() {
                    var e = this.$game.querySelector("game-modal");
                    e.appendChild(document.createElement("game-help")), e.setAttribute("open", "")
                }
            }, {
                key: "connectedCallback",
                value: function() {
                    var e, a, s, t, n, o, r, i, l, d = this;
                    this.shadowRoot.appendChild(rs.content.cloneNode(!0)), this.$game = this.shadowRoot.querySelector("#game"), this.$board = this.shadowRoot.querySelector("#board"), this.$keyboard = this.shadowRoot.querySelector("game-keyboard"), this.sizeBoard(), this.lastPlayedTs || setTimeout((function() {
                        return d.showHelpModal()
                    }), 100);
                    for (var c = 0; c < 6; c++) {
                        var u = document.createElement("game-row");
                        u.setAttribute("letters", this.boardState[c]), u.setAttribute("length", FLAG.length), this.evaluations[c] && (u.evaluation = this.evaluations[c]), this.$board.appendChild(u)
                    }
                    this.$game.addEventListener("game-key-press", (function(e) {
                            var a = e.detail.key;
                            "←" === a || "Backspace" === a ? d.removeLetter() : "↵" === a || "Enter" === a ? d.submitGuess() : Wa.includes(a.toLowerCase()) && d.addLetter(a.toLowerCase())
                        })), this.$game.addEventListener("game-last-tile-revealed-in-row", (function(e) {
                            d.$keyboard.letterEvaluations = d.letterEvaluations, d.rowIndex < 6 && (d.canInput = !0);
                            var a = d.$board.querySelectorAll("game-row")[d.rowIndex - 1];
                            (e.path || e.composedPath && e.composedPath()).includes(a) && ([ds, cs].includes(d.gameStatus) && (d.restoringFromLocalStorage ? d.showStatsModal() : (d.gameStatus === ds && (a.setAttribute("win", ""), d.addToast(us[d.rowIndex - 1], 2e3)), d.gameStatus === cs && d.addToast(d.solution.toUpperCase(), 1 / 0), setTimeout((function() {
                                d.showStatsModal()
                            }), 2500))), d.restoringFromLocalStorage = !1)
                        })), this.shadowRoot.addEventListener("game-setting-change", (function(e) {
                            var a = e.detail,
                                s = a.name,
                                t = a.checked,
                                n = a.disabled;
                            switch (s) {
                                case "hard-mode":
                                    return void(n ? d.addToast("Hard mode can only be enabled at the start of a round", 1500, !0) : (d.hardMode = t, ja({
                                        hardMode: t
                                    })))
                            }
                        })), this.shadowRoot.getElementById("settings-button").addEventListener("click", (function(e) {
                            var a = d.$game.querySelector("game-page"),
                                s = document.createTextNode("Settings");
                            a.appendChild(s);
                            var t = document.createElement("game-settings");
                            t.setAttribute("slot", "content"), t.gameApp = d, a.appendChild(t), a.setAttribute("open", "")
                        })), this.shadowRoot.getElementById("help-button").addEventListener("click", (function(e) {
                            var a = d.$game.querySelector("game-page"),
                                s = document.createTextNode("How to play");
                            a.appendChild(s);
                            var t = document.createElement("game-help");
                            t.setAttribute("page", ""), t.setAttribute("slot", "content"), a.appendChild(t), a.setAttribute("open", "")
                        })), this.shadowRoot.getElementById("statistics-button").addEventListener("click", (function(e) {
                            d.showStatsModal()
                        })), this.shadowRoot.getElementById("nav-button").addEventListener("click", (function(e) {
                            d.showNavModal()
                        })), window.addEventListener("resize", this.sizeBoard.bind(this)), os(), i = {
                            container: "GTM-P528B3",
                            prdstring: "&gtm_auth=tfAzqo1rYDLgYhmTnSjPqw&gtm_preview=env-130",
                            devstring: "&gtm_auth=WiJyA7zv1sohHCWSZ3mF1Q&gtm_preview=env-8",
                            stgstring: "&gtm_auth=FOuAsPhG-4kWeLk6Kq5AzQ&gtm_preview=env-7",
                            dataLayer: "",
                            modifier: "",
                            env: document.location.host.indexOf(".dev.") > -1 ? "dev" : document.location.host.indexOf(".stg.") > -1 || document.location.host.indexOf(".stage.") > -1 ? "stg" : "prod"
                        }, l = {
                            event: "pageDataReady",
                            application: {
                                name: "games-crosswords",
                                environment: i.env
                            }
                        }, i.modifier = i.prdstring, "dev" === i.env ? i.modifier = i.devstring : "stg" === i.env && (i.modifier = i.stgstring),
                        function(e, a, s, t, n, o) {
                            e[t] = e[t] || [], e[t].push({
                                "gtm.start": (new Date).getTime(),
                                event: "gtm.js"
                            });
                            var r = a.getElementsByTagName(s)[0],
                                i = a.createElement(s);
                            i.async = !0, i.src = "https://www.googletagmanager.com/gtm.js?id=" + n + o + "&gtm_cookies_win=x", r.parentNode.insertBefore(i, r)
                        }(window, document, "script", "dataLayer", i.container, i.modifier), e = l, a = i.env, t = a && "prod" === a ? "a.nytimes.com" : "a.dev.nytimes.com", n = encodeURIComponent(document.referrer), o = encodeURIComponent((s = document.querySelector("link[rel=canonical]")) ? s.href : document.location.href), (r = new XMLHttpRequest).withCredentials = !0, r.open("GET", "https://" + t + "/svc/nyt/data-layer?sourceApp=" + e.application.name + "&referrer=" + n + "&assetUrl=" + o, !0), r.onload = function() {
                            var a = JSON.parse(r.responseText);
                            a.event = "userDataReady", window.dataLayer.push(a), window.dataLayer.push(e)
                        }, r.addEventListener("error", (function() {
                            window.dataLayer.push(e)
                        })), r.send()
                }
            }, {
                key: "disconnectedCallback",
                value: function() {
                    clearInterval(this.refreshTimer)
                }
            }, {
                key: "debugTools",
                value: function() {
                    var e = this;
                    this.shadowRoot.getElementById("debug-tools").appendChild(is.content.cloneNode(!0)), this.shadowRoot.getElementById("toast").addEventListener("click", (function(a) {
                        e.addToast("hello world")
                    })), this.shadowRoot.getElementById("modal").addEventListener("click", (function(a) {
                        var s = e.$game.querySelector("game-modal");
                        s.textContent = "hello plz", s.setAttribute("open", "")
                    })), this.shadowRoot.getElementById("reveal").addEventListener("click", (function() {
                        e.evaluateRow()
                    })), this.shadowRoot.getElementById("shake").addEventListener("click", (function() {
                        e.$board.querySelectorAll("game-row")[e.rowIndex].setAttribute("invalid", "")
                    })), this.shadowRoot.getElementById("bounce").addEventListener("click", (function() {
                        var a = e.$board.querySelectorAll("game-row")[e.rowIndex - 1];
                        "" === a.getAttribute("win") ? a.removeAttribute("win") : a.setAttribute("win", "")
                    }))
                }
            }]), t
        }(u(HTMLElement));
    customElements.define("game-app", ms);
    var ps = document.createElement("template");
    ps.innerHTML = "\n  <style>\n    .overlay {\n      display: none;\n      position: absolute;\n      width: 100%;\n      height: 100%;\n      top: 0;\n      left: 0;\n      justify-content: center;\n      align-items: center;\n      background-color: var(--opacity-50);\n      z-index: ".concat(3e3, ';\n    }\n\n    :host([open]) .overlay {\n      display: flex;\n    }\n\n    .content {\n      position: relative;\n      border-radius: 8px;\n      border: 1px solid var(--color-tone-6);\n      background-color: var(--modal-content-bg);\n      color: var(--color-tone-1);\n      box-shadow: 0 4px 23px 0 rgba(0, 0, 0, 0.2);\n      width: 90%;\n      max-height: 90%;\n      overflow-y: auto;\n      animation: SlideIn 200ms;\n      max-width: var(--game-max-width);\n      padding: 16px;\n      box-sizing: border-box;\n    }\n\n    .content.closing {\n      animation: SlideOut 200ms;\n    }\n\n    .close-icon {\n      width: 24px;\n      height: 24px;\n      position: absolute;\n      top: 16px;\n      right: 16px;\n    }\n\n    game-icon {\n      position: fixed;\n      user-select: none;\n      cursor: pointer;\n    }\n\n    @keyframes SlideIn {\n      0% {\n        transform: translateY(30px);\n        opacity: 0;\n      }\n      100% {\n        transform: translateY(0px);\n        opacity: 1;\n      }\n    }\n    @keyframes SlideOut {\n      0% {\n        transform: translateY(0px);\n        opacity: 1;\n      }\n      90% {\n        opacity: 0;\n      }\n      100% {\n        opacity: 0;\n        transform: translateY(60px);\n      }\n    }\n  </style>\n  <div class="overlay">\n    <div class="content">\n      <slot></slot>\n      <div class="close-icon">\n        <game-icon icon="close"></game-icon>\n      </div>\n    </div>\n  </div>\n');
    var hs = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), (e = a.call(this)).attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "connectedCallback",
            value: function() {
                var e = this;
                this.shadowRoot.appendChild(ps.content.cloneNode(!0)), this.addEventListener("click", (function(a) {
                    e.shadowRoot.querySelector(".content").classList.add("closing")
                })), this.shadowRoot.addEventListener("animationend", (function(a) {
                    "SlideOut" === a.animationName && (e.shadowRoot.querySelector(".content").classList.remove("closing"), e.removeChild(e.firstChild), e.removeAttribute("open"))
                }))
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("game-modal", hs);
    var ys = document.createElement("template");
    ys.innerHTML = "\n  <style>\n  :host {\n    height: var(--keyboard-height);\n  }\n  #keyboard {\n    margin: 0 8px;\n    user-select: none;\n  }\n  \n  .row {\n    display: flex;\n    width: 100%;\n    margin: 0 auto 8px;\n    /* https://stackoverflow.com/questions/46167604/ios-html-disable-double-tap-to-zoom */\n    touch-action: manipulation;\n  }\n  \n  button {\n    font-family: inherit;\n    font-weight: bold;\n    border: 0;\n    padding: 0;\n    margin: 0 6px 0 0;\n    height: 58px;\n    border-radius: 4px;\n    cursor: pointer;\n    user-select: none;\n    background-color: var(--key-bg);\n    color: var(--key-text-color);\n    flex: 1;\n    display: flex;\n    justify-content: center;\n    align-items: center;\n    text-transform: uppercase;\n    -webkit-tap-highlight-color: rgba(0,0,0,0.3);\n  }\n\n  button:focus {\n    outline: none;\n  }\n\n  button.fade {\n    transition: background-color 0.1s ease, color 0.1s ease;\n  }\n  \n  button:last-of-type {\n    margin: 0;\n  }\n  \n  .half {\n    flex: 0.5;\n  }\n  \n  .one {\n    flex: 1;\n  }\n\n  .one-and-a-half {\n    flex: 1.5;\n    font-size: 12px;\n  }\n  \n  .two {\n    flex: 2;\n  }\n\n  button[data-state='correct'] {\n    background-color: var(--key-bg-correct);\n    color: var(--key-evaluated-text-color);\n  }\n\n  button[data-state='present'] {\n    background-color: var(--key-bg-present);\n    color: var(--key-evaluated-text-color);\n  }\n\n  button[data-state='absent'] {\n    background-color: var(--key-bg-absent);\n    color: var(--key-evaluated-text-color);\n  }\n\n  </style>\n  <div id=\"keyboard\"></div>\n";
    var gs = document.createElement("template");
    gs.innerHTML = "\n  <button>key</button>\n";
    var bs = document.createElement("template");
    bs.innerHTML = '\n  <div class="spacer"></div>\n';
    var fs = [
            ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "{", "}", "_"],
            ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
            ["-", "a", "s", "d", "f", "g", "h", "j", "k", "l", "-"],
            ["↵", "z", "x", "c", "v", "b", "n", "m", "←"]
        ],
        ks = function(e) {
            r(t, e);
            var a = h(t);

            function t() {
                var e;
                return s(this, t), o(m(e = a.call(this)), "_letterEvaluations", {}), e.attachShadow({
                    mode: "open"
                }), e
            }
            return n(t, [{
                key: "letterEvaluations",
                set: function(e) {
                    this._letterEvaluations = e, this._render()
                }
            }, {
                key: "dispatchKeyPressEvent",
                value: function(e) {
                    this.dispatchEvent(new CustomEvent("game-key-press", {
                        bubbles: !0,
                        composed: !0,
                        detail: {
                            key: e
                        }
                    }))
                }
            }, {
                key: "connectedCallback",
                value: function() {
                    var e = this;
                    this.shadowRoot.appendChild(ys.content.cloneNode(!0)), this.$keyboard = this.shadowRoot.getElementById("keyboard"), this.$keyboard.addEventListener("click", (function(a) {
                        var s = a.target.closest("button");
                        s && e.$keyboard.contains(s) && e.dispatchKeyPressEvent(s.dataset.key)
                    })), window.addEventListener("keydown", (function(a) {
                        if (!0 !== a.repeat) {
                            var s = a.key,
                                t = a.metaKey,
                                n = a.ctrlKey;
                            t || n || (Wa.includes(s.toLowerCase()) || "Backspace" === s || "Enter" === s) && e.dispatchKeyPressEvent(s)
                        }
                    })), this.$keyboard.addEventListener("transitionend", (function(a) {
                        var s = a.target.closest("button");
                        s && e.$keyboard.contains(s) && s.classList.remove("fade")
                    })), fs.forEach((function(a) {
                        var s = document.createElement("div");
                        s.classList.add("row"), a.forEach((function(e) {
                            var a;
                            if (e >= "0" && e <= "9" || e >= "a" && e <= "z" || "←" === e || "↵" === e || e === "{" || e === "}" || e === "_") {
                                if ((a = gs.content.cloneNode(!0).firstElementChild).dataset.key = e, a.textContent = e, "←" === e) {
                                    var t = document.createElement("game-icon");
                                    t.setAttribute("icon", "backspace"), a.textContent = "", a.appendChild(t), a.classList.add("one-and-a-half")
                                }
                                "↵" == e && (a.textContent = "enter", a.classList.add("one-and-a-half"))
                            } else(a = bs.content.cloneNode(!0).firstElementChild).classList.add(1 === e.length ? "half" : "one");
                            s.appendChild(a)
                        })), e.$keyboard.appendChild(s)
                    })), this._render()
                }
            }, {
                key: "_render",
                value: function() {
                    for (var e in this._letterEvaluations) {
                        var a = this.$keyboard.querySelector('[data-key="'.concat(e, '"]'));
                        a.dataset.state = this._letterEvaluations[e], a.classList.add("fade")
                    }
                }
            }]), t
        }(u(HTMLElement));
    /*! *****************************************************************************
      Copyright (c) Microsoft Corporation.

      Permission to use, copy, modify, and/or distribute this software for any
      purpose with or without fee is hereby granted.

      THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
      REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
      AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
      INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
      LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
      OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
      PERFORMANCE OF THIS SOFTWARE.
      ***************************************************************************** */
    function vs(e, a, s, t) {
        return new(s || (s = Promise))((function(n, o) {
            function r(e) {
                try {
                    l(t.next(e))
                } catch (e) {
                    o(e)
                }
            }

            function i(e) {
                try {
                    l(t.throw(e))
                } catch (e) {
                    o(e)
                }
            }

            function l(e) {
                var a;
                e.done ? n(e.value) : (a = e.value, a instanceof s ? a : new s((function(e) {
                    e(a)
                }))).then(r, i)
            }
            l((t = t.apply(e, a || [])).next())
        }))
    }

    function ws(e, a) {
        var s, t, n, o, r = {
            label: 0,
            sent: function() {
                if (1 & n[0]) throw n[1];
                return n[1]
            },
            trys: [],
            ops: []
        };
        return o = {
            next: i(0),
            throw: i(1),
            return: i(2)
        }, "function" == typeof Symbol && (o[Symbol.iterator] = function() {
            return this
        }), o;

        function i(o) {
            return function(i) {
                return function(o) {
                    if (s) throw new TypeError("Generator is already executing.");
                    for (; r;) try {
                        if (s = 1, t && (n = 2 & o[0] ? t.return : o[0] ? t.throw || ((n = t.return) && n.call(t), 0) : t.next) && !(n = n.call(t, o[1])).done) return n;
                        switch (t = 0, n && (o = [2 & o[0], n.value]), o[0]) {
                            case 0:
                            case 1:
                                n = o;
                                break;
                            case 4:
                                return r.label++, {
                                    value: o[1],
                                    done: !1
                                };
                            case 5:
                                r.label++, t = o[1], o = [0];
                                continue;
                            case 7:
                                o = r.ops.pop(), r.trys.pop();
                                continue;
                            default:
                                if (!((n = (n = r.trys).length > 0 && n[n.length - 1]) || 6 !== o[0] && 2 !== o[0])) {
                                    r = 0;
                                    continue
                                }
                                if (3 === o[0] && (!n || o[1] > n[0] && o[1] < n[3])) {
                                    r.label = o[1];
                                    break
                                }
                                if (6 === o[0] && r.label < n[1]) {
                                    r.label = n[1], n = o;
                                    break
                                }
                                if (n && r.label < n[2]) {
                                    r.label = n[2], r.ops.push(o);
                                    break
                                }
                                n[2] && r.ops.pop(), r.trys.pop();
                                continue
                        }
                        o = a.call(e, r)
                    } catch (e) {
                        o = [6, e], t = 0
                    } finally {
                        s = n = 0
                    }
                    if (5 & o[0]) throw o[1];
                    return {
                        value: o[0] ? o[1] : void 0,
                        done: !0
                    }
                }([o, i])
            }
        }
    }
    customElements.define("game-keyboard", ks),
        function() {
            (console.warn || console.log).apply(console, arguments)
        }.bind("[clipboard-polyfill]");
    var xs, zs, js, Ss, Cs = "undefined" == typeof navigator ? void 0 : navigator,
        Es = null == Cs ? void 0 : Cs.clipboard;
    null === (xs = null == Es ? void 0 : Es.read) || void 0 === xs || xs.bind(Es), null === (zs = null == Es ? void 0 : Es.readText) || void 0 === zs || zs.bind(Es);
    var _s = (null === (js = null == Es ? void 0 : Es.write) || void 0 === js || js.bind(Es), null === (Ss = null == Es ? void 0 : Es.writeText) || void 0 === Ss ? void 0 : Ss.bind(Es)),
        qs = "undefined" == typeof window ? void 0 : window,
        Ls = (null == qs || qs.ClipboardItem, qs);
    var Ts = function() {
        this.success = !1
    };

    function As(e, a, s) {
        for (var t in e.success = !0, a) {
            var n = a[t],
                o = s.clipboardData;
            o.setData(t, n), "text/plain" === t && o.getData(t) !== n && (e.success = !1)
        }
        s.preventDefault()
    }

    function Is(e) {
        var a = new Ts,
            s = As.bind(this, a, e);
        document.addEventListener("copy", s);
        try {
            document.execCommand("copy")
        } finally {
            document.removeEventListener("copy", s)
        }
        return a.success
    }

    function Ms(e, a) {
        Os(e);
        var s = Is(a);
        return Rs(), s
    }

    function Os(e) {
        var a = document.getSelection();
        if (a) {
            var s = document.createRange();
            s.selectNodeContents(e), a.removeAllRanges(), a.addRange(s)
        }
    }

    function Rs() {
        var e = document.getSelection();
        e && e.removeAllRanges()
    }

    function Hs(e) {
        return vs(this, void 0, void 0, (function() {
            var a;
            return ws(this, (function(s) {
                if (a = "text/plain" in e, "undefined" == typeof ClipboardEvent && void 0 !== Ls.clipboardData && void 0 !== Ls.clipboardData.setData) {
                    if (!a) throw new Error("No `text/plain` value was specified.");
                    if (t = e["text/plain"], Ls.clipboardData.setData("Text", t)) return [2, !0];
                    throw new Error("Copying failed, possibly because the user rejected it.")
                }
                var t;
                return Is(e) || navigator.userAgent.indexOf("Edge") > -1 || Ms(document.body, e) || function(e) {
                    var a = document.createElement("div");
                    a.setAttribute("style", "-webkit-user-select: text !important"), a.textContent = "temporary element", document.body.appendChild(a);
                    var s = Ms(a, e);
                    return document.body.removeChild(a), s
                }(e) || function(e) {
                    var a = document.createElement("div");
                    a.setAttribute("style", "-webkit-user-select: text !important");
                    var s = a;
                    a.attachShadow && (s = a.attachShadow({
                        mode: "open"
                    }));
                    var t = document.createElement("span");
                    t.innerText = e, s.appendChild(t), document.body.appendChild(a), Os(t);
                    var n = document.execCommand("copy");
                    return Rs(), document.body.removeChild(a), n
                }(e["text/plain"]) ? [2, !0] : [2, !1]
            }))
        }))
    }

    function Ns(e, a, s) {
        try {
            Sa() && !(navigator.userAgent.toLowerCase().indexOf("firefox") > -1) && void 0 !== navigator.share && navigator.canShare && navigator.canShare(e) ? navigator.share(e) : function(e) {
                return vs(this, void 0, void 0, (function() {
                    return ws(this, (function(a) {
                        if (_s) return [2, _s(e)];
                        if (!Hs(function(e) {
                                var a = {};
                                return a["text/plain"] = e, a
                            }(e))) throw new Error("writeText() failed");
                        return [2]
                    }))
                }))
            }(e.text).then(a, s)
        } catch (e) {
            s()
        }
    }
    var Ps = document.createElement("template");
    Ps.innerHTML = '\n  <style>\n    .container {\n      display: flex;\n      flex-direction: column;\n      align-items: center;\n      justify-content: center;\n      padding: 16px 0; \n    }\n    h1 {\n      font-weight: 700;\n      font-size: 16px;\n      letter-spacing: 0.5px;\n      text-transform: uppercase;\n      text-align: center;\n      margin-bottom: 10px;\n    }\n  \n    #statistics {\n      display: flex;\n      margin-bottom: \n    }\n\n    .statistic-container {\n      flex: 1;\n    }\n\n    .statistic-container .statistic {\n      font-size: 36px;\n      font-weight: 400;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      text-align: center;\n      letter-spacing: 0.05em;\n      font-variant-numeric: proportional-nums;\n    }\n\n    .statistic.timer {\n      font-variant-numeric: initial;\n    }\n\n    .statistic-container .label {\n      font-size: 12px;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      text-align: center;\n    }\n\n    #guess-distribution {\n      width: 80%;\n    }\n\n    .graph-container {\n      width: 100%;\n      height: 20px;\n      display: flex;\n      align-items: center;\n      padding-bottom: 4px;\n      font-size: 14px;\n      line-height: 20px;\n    }\n\n    .graph-container .graph {\n      width: 100%;\n      height: 100%;\n      padding-left: 4px;\n    }\n\n    .graph-container .graph .graph-bar {\n      height: 100%;\n      /* Assume no wins */\n      width: 0%;\n      position: relative;\n      background-color: var(--color-absent);\n      display: flex;\n      justify-content: center;\n    }\n\n    .graph-container .graph .graph-bar.highlight {\n      background-color: var(--color-correct);\n    }\n\n    .graph-container .graph .graph-bar.align-right {\n      justify-content: flex-end;\n      padding-right: 8px;\n    }\n\n    .graph-container .graph .num-guesses {\n      font-weight: bold;\n      color: var(--tile-text-color);\n    }\n\n    #statistics,\n    #guess-distribution {\n      padding-bottom: 10px;\n    }\n\n    .footer {\n      display: flex;\n      width: 100%;\n    }\n\n    .countdown {\n      border-right: 1px solid var(--color-tone-1);\n      padding-right: 12px;\n      width: 50%;\n    }\n\n    .share {\n      display: flex;\n      justify-content: center;\n      align-items: center;\n      padding-left: 12px;\n      width: 50%;\n    }\n\n    .no-data {\n      text-align: center;\n    }\n\n    button#share-button {\n      background-color: var(--key-bg-correct);\n      color: var(--key-evaluated-text-color);\n      font-family: inherit;\n      font-weight: bold;\n      border-radius: 4px;\n      cursor: pointer;\n      border: none;\n      user-select: none;\n      display: flex;\n      justify-content: center;\n      align-items: center;\n      text-transform: uppercase;\n      -webkit-tap-highlight-color: rgba(0,0,0,0.3);\n      width: 80%;\n      font-size: 20px;\n      height: 52px;\n      -webkit-filter: brightness(100%);\n    }\n    button#share-button:hover {\n      opacity: 0.9;\n    }\n    button#share-button game-icon {\n      width: 24px;\n      height: 24px;\n      padding-left: 8px;\n    }\n  </style>\n\n  <div class="container">\n    <h1>Statistics</h1>\n    <div id="statistics"></div>\n    <h1>Guess Distribution</h1>\n    <div id="guess-distribution"></div>\n    <div class="footer"></div>\n  </div>\n';
    var $s = document.createElement("template");
    $s.innerHTML = '\n  <div class="statistic-container">\n    <div class="statistic"></div>\n    <div class="label"></div>\n  </div>\n';
    var Ds = document.createElement("template");
    Ds.innerHTML = '\n    <div class="graph-container">\n      <div class="guess"></div>\n      <div class="graph">\n        <div class="graph-bar">\n          <div class="num-guesses">\n        </div>\n      </div>\n      </div>\n    </div>\n';
    var Bs = document.createElement("template");
    Bs.innerHTML = '\n  <div class="countdown">\n    <h1>Next FLAGLE</h1>\n    <div id="timer">\n      <div class="statistic-container">\n        <div class="statistic timer">\n          <countdown-timer></countdown-timer>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="share">\n    <button id="share-button">\n      Share <game-icon icon="share"></game-icon>\n    </button>\n  </div>\n';
    var Gs = {
            currentStreak: "Current Streak",
            maxStreak: "Max Streak",
            winPercentage: "Win %",
            gamesPlayed: "Played",
            gamesWon: "Won",
            averageGuesses: "Av. Guesses"
        },
        Vs = function(e) {
            r(t, e);
            var a = h(t);

            function t() {
                var e;
                return s(this, t), o(m(e = a.call(this)), "stats", {}), o(m(e), "gameApp", void 0), e.attachShadow({
                    mode: "open"
                }), e.stats = Xa(), e
            }
            return n(t, [{
                key: "connectedCallback",
                value: function() {
                    var e = this;
                    this.shadowRoot.appendChild(Ps.content.cloneNode(!0));
                    var a = this.shadowRoot.getElementById("statistics"),
                        s = this.shadowRoot.getElementById("guess-distribution"),
                        t = Math.max.apply(Math, g(Object.values(this.stats.guesses)));
                    if (Object.values(this.stats.guesses).every((function(e) {
                            return 0 === e
                        }))) {
                        var n = document.createElement("div");
                        n.classList.add("no-data"), n.innerText = "No Data", s.appendChild(n)
                    } else
                        for (var o = 1; o < Object.keys(this.stats.guesses).length; o++) {
                            var r = o,
                                i = this.stats.guesses[o],
                                l = Ds.content.cloneNode(!0),
                                d = Math.max(7, Math.round(i / t * 100));
                            l.querySelector(".guess").textContent = r;
                            var c = l.querySelector(".graph-bar");
                            if (c.style.width = "".concat(d, "%"), "number" == typeof i) {
                                l.querySelector(".num-guesses").textContent = i, i > 0 && c.classList.add("align-right");
                                var u = parseInt(this.getAttribute("highlight-guess"), 10);
                                u && o === u && c.classList.add("highlight")
                            }
                            s.appendChild(l)
                        }
                    if (["gamesPlayed", "winPercentage", "currentStreak", "maxStreak"].forEach((function(s) {
                            var t = Gs[s],
                                n = e.stats[s],
                                o = $s.content.cloneNode(!0);
                            o.querySelector(".label").textContent = t, o.querySelector(".statistic").textContent = n, a.appendChild(o)
                        })), this.gameApp.gameStatus !== ls) {
                        var m = this.shadowRoot.querySelector(".footer"),
                            p = Bs.content.cloneNode(!0);
                        m.appendChild(p), this.shadowRoot.querySelector("button#share-button").addEventListener("click", (function(a) {
                            a.preventDefault(), a.stopPropagation();
                            Ns(function(e) {
                                var a = e.evaluations,
                                    s = e.dayOffset,
                                    t = e.rowIndex,
                                    n = e.isHardMode,
                                    o = e.isWin,
                                    r = JSON.parse(window.localStorage.getItem(j)),
                                    i = JSON.parse(window.localStorage.getItem(S)),
                                    l = "Flagle 1";
                                l += " ".concat(o ? t : "X", "/").concat(6), n && (l += "*");
                                var d = "";
                                return a.forEach((function(e) {
                                    e && (e.forEach((function(e) {
                                        if (e) {
                                            var a = "";
                                            switch (e) {
                                                case Ha:
                                                    a = function(e) {
                                                        return e ? "🟧" : "🟩"
                                                    }(i);
                                                    break;
                                                case Ra:
                                                    a = function(e) {
                                                        return e ? "🟦" : "🟨"
                                                    }(i);
                                                    break;
                                                case Na:
                                                    a = function(e) {
                                                        return e ? "⬛" : "⬜"
                                                    }(r)
                                            }
                                            d += a
                                        }
                                    })), d += "\n")
                                })), {
                                    text: "".concat(l, "\n\n").concat(d.trimEnd())
                                }
                            }({
                                evaluations: e.gameApp.evaluations,
                                dayOffset: e.gameApp.dayOffset,
                                rowIndex: e.gameApp.rowIndex,
                                isHardMode: e.gameApp.hardMode,
                                isWin: e.gameApp.gameStatus === ds
                            }), (function() {
                                e.gameApp.addToast("Copied results to clipboard", 2e3, !0)
                            }), (function() {
                                e.gameApp.addToast("Share failed", 2e3, !0)
                            }))
                        }))
                    }
                }
            }]), t
        }(u(HTMLElement));
    customElements.define("game-stats", Vs);
    var Fs = document.createElement("template"),
        Ws = [{
            id: "spelling-bee",
            name: "Spelling Bee",
            url: "/puzzles/spelling-bee",
            backgroundImage: "var(--spelling-bee)"
        }, {
            id: "crossword",
            name: "The Crossword",
            url: "/crosswords/game/daily",
            backgroundImage: "var(--daily)"
        }, {
            id: "mini",
            name: "The Mini",
            url: "/crosswords/game/mini",
            backgroundImage: "var(--mini)"
        }, {
            id: "tiles",
            name: "Tiles",
            url: "/puzzles/tiles",
            backgroundImage: "var(--tiles)"
        }, {
            id: "sudoku",
            name: "Sudoku",
            url: "/puzzles/sudoku",
            backgroundImage: "var(--sudoku)"
        }, {
            id: "vertex",
            name: "Vertex",
            url: "/puzzles/vertex",
            backgroundImage: "var(--vertex)"
        }, {
            id: "letter-boxed",
            name: "Letter Boxed",
            url: "/puzzles/letter-boxed",
            backgroundImage: "var(--letter-boxed)"
        }, {
            id: "all-games",
            name: "All Games",
            url: "/puzzles"
        }].map((function(e) {
            return "\n    <a href=".concat(e.url, " id=").concat(e.id, '>\n      <div class="nav-item" style="--hover-color: var(--color-nav-hover)">\n        <span style="background-image: ').concat(e.backgroundImage, '; background-size: 20px;"class="nav-icon"></span>\n          ').concat(e.name, " \n      </div>\n    </a>\n    ")
        })).join("");
    Fs.innerHTML = "\n  <style>\n    .container {\n      display: flex;\n      flex-direction: column;\n      align-items: left;\n      justify-content: center;\n    }\n    h1 {\n      font-weight: 700;\n      font-size: 16px;\n      letter-spacing: 0.5px;\n      text-transform: uppercase;\n      text-align: center;\n      margin-bottom: 10px;\n    }\n\n    .nav-container {\n      flex: 1;\n    }\n\n    .nav-container .nav {\n      font-size: 36px;\n      font-weight: 400;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      text-align: center;\n      letter-spacing: 0.05em;\n      font-variant-numeric: proportional-nums;\n    }\n\n    .nav-container .label {\n      font-size: 12px;\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      text-align: center;\n    }\n\n    .nav-list {\n        list-style: none;\n        color: var(--color-tone-1);\n        padding: unset;\n        margin: unset;\n    }\n\n    .nav-item {\n        display: flex;\n        justify-content: left;\n        align-items: center;\n        height: 40px;\n        font-weight: 500;\n        font-family: 'nyt-franklin';\n        font-size: 16px;\n        line-height: 16px;\n        padding-left: 18px;\n    }\n\n    .nav-item:hover {\n        background-color: var(--hover-color);\n    }\n\n    .nav-icon {\n        padding-bottom: 2px;\n        content: '';\n        height: 20px;\n        width: 28px;\n        padding-right: 8px;\n        display: inline-block;\n        vertical-align: middle;\n        background-repeat: no-repeat;\n    }\n\n    #nav {\n      padding-bottom: 10px;\n    }\n\n    a {\n        text-decoration: none;\n        color: inherit;\n    }\n\n    .more-text {\n        font-family: 'nyt-franklin-700';\n        font-weight: 700;\n        text-transform: uppercase;\n        font-size: 12px;\n        line-height: 12px;\n        margin: 32px 0px 24px 0px;\n        padding-left: 18px;\n    }\n\n    .nav-header {\n        padding-top: 18px;\n        padding-left: 18px;\n    }\n\n    .privacy {\n      letter-spacing: .5px;\n      font-family: 'nyt-franklin';\n      position: absolute;\n      bottom: 0;\n      left: 0;\n      right: 0;\n      margin: 0px 25px 0px 17px;\n      padding: 12px 0px;\n      border-top: 1px solid #DCDCDC;\n      color: var(--color-tone-1);\n      font-size: 15px;\n      text-align: right;\n      display: flex;\n      justify-content: space-between;\n      align-items: flex-end;\n    }\n  </style>\n\n  <div class=\"container\">\n    <span class=\"nav-header\">\n        <nyt-icon></nyt-icon>\n    </span>\n    <span class=\"more-text\">More New York Times Games</span>\n    <div class=\"nav-list\">".concat(Ws, '</div>\n    <div class="privacy">\n      <a href="https://www.nytimes.com/privacy/privacy-policy" onmouseover="this.style.textDecoration=\'underline\';" \n      onmouseout="this.style.textDecoration=\'none\';">\n        Privacy Policy\n      </a>\n    </div>\n  </div>\n');
    var Ys = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), o(m(e = a.call(this)), "gameApp", void 0), e.attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "connectedCallback",
            value: function() {
                this.shadowRoot.appendChild(Fs.content.cloneNode(!0))
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("game-nav", Ys);
    var Us = document.createElement("template");
    Us.innerHTML = "\n  <style>\n    .overlay-nav {\n      display: none;\n      position: absolute;\n      width: 100%;\n      height: 100%;\n      top: 0;\n      left: 0;\n      z-index: ".concat(3e3, ';\n      background-color: transparent;\n      justify-content: left;\n      align-items: unset;\n    }\n\n    :host([open]) .overlay-nav {\n      display: flex;\n    }\n\n    .content-nav {\n      position: relative;\n      border: 1px solid var(--color-tone-6);\n      background-color: var(--modal-content-bg);\n      color: var(--color-tone-1);\n      overflow-y: auto;\n      animation: SlideRight 200ms;\n      max-width: var(--game-max-width);\n      box-sizing: border-box;\n      width: 100%;\n      border-radius: 0px;\n      box-shadow: 3px 5px 5px rgba(0, 0, 0, 0.15);\n      max-height: calc(100% - var(--header-height) - 1px);\n      margin-top: calc(var(--header-height) + 1px);\n      padding: 0px;\n    }\n\n    @media (min-width: 415px) {\n      .content-nav {\n        width: 375px;\n      }\n    }\n\n    .content-nav.closing-nav {\n      animation: SlideLeft 200ms;\n    }\n\n    .close-icon-nav {\n      width: 24px;\n      height: 24px;\n      position: absolute;\n      top: 16px;\n      right: 16px;\n    }\n\n    game-icon {\n      position: fixed;\n      user-select: none;\n      cursor: pointer;\n    }\n\n    @keyframes SlideRight {\n      0% {\n        transform: translateX(-100px);\n        opacity: 0;\n      }\n      100% {\n        transform: translateX(0px);\n        opacity: 1;\n      }\n    }\n    @keyframes SlideLeft {\n      0% {\n        transform: translateX(0px);\n        opacity: 1;\n      }\n      90% {\n        opacity: 0;\n      }\n      100% {\n        opacity: 0;\n        transform: translateX(-200px);\n      }\n    }\n  </style>\n  <div class="overlay-nav">\n    <div class="content-nav">\n      <slot></slot>\n      <div class="close-icon-nav">\n        <game-icon icon="close"></game-icon>\n      </div>\n    </div>\n  </div>\n');
    var Js = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), (e = a.call(this)).attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "connectedCallback",
            value: function() {
                var e = this;
                this.shadowRoot.appendChild(Us.content.cloneNode(!0)), this.addEventListener("click", (function(a) {
                    e.shadowRoot.querySelector(".content-nav").classList.add("closing-nav")
                })), this.shadowRoot.addEventListener("animationend", (function(a) {
                    "SlideLeft" === a.animationName && (e.shadowRoot.querySelector(".content-nav").classList.remove("closing-nav"), e.removeChild(e.firstChild), e.removeAttribute("open"))
                }))
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("game-nav-modal", Js);
    var Xs = document.createElement("template");
    Xs.innerHTML = '\n  <style>\n    :host {\n    }\n    .container {\n      display: flex;\n      justify-content: space-between;\n    }\n    .switch {\n      height: 20px;\n      width: 32px;\n      vertical-align: middle;\n      /* not quite right */\n      background: var(--color-tone-3);\n      border-radius: 999px;\n      display: block;\n      position: relative;\n    }\n    .knob {\n      display: block;\n      position: absolute;\n      left: 2px;\n      top: 2px;\n      height: calc(100% - 4px);\n      width: 50%;\n      border-radius: 8px;\n      background: var(--white);\n      transform: translateX(0);\n      transition: transform 0.3s;\n    }\n    :host([checked]) .switch {\n      background: var(--color-correct);\n    }\n    :host([checked]) .knob {\n      transform: translateX(calc(100% - 4px));\n    }\n    :host([disabled]) .switch {\n      opacity: 0.5;\n    }\n  </style>\n  <div class="container">\n    <label><slot></slot></label>\n    <div class="switch">\n      <span class="knob"></div>\n    </div>\n  </div>\n';
    var Zs = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), (e = a.call(this)).attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "connectedCallback",
            value: function() {
                var e = this;
                this.shadowRoot.appendChild(Xs.content.cloneNode(!0)), this.shadowRoot.querySelector(".container").addEventListener("click", (function(a) {
                    a.stopPropagation(), e.hasAttribute("checked") ? e.removeAttribute("checked") : e.setAttribute("checked", ""), e.dispatchEvent(new CustomEvent("game-switch-change", {
                        bubbles: !0,
                        composed: !0,
                        detail: {
                            name: e.getAttribute("name"),
                            checked: e.hasAttribute("checked"),
                            disabled: e.hasAttribute("disabled")
                        }
                    }))
                }))
            }
        }], [{
            key: "observedAttributes",
            get: function() {
                return ["checked"]
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("game-switch", Zs);
    var Ks = document.createElement("template");
    Ks.innerHTML = '\n  <style>\n  .instructions {\n    font-size: 14px;\n    color: var(--color-tone-1)\n  }\n\n  .examples {\n    border-bottom: 1px solid var(--color-tone-4);\n    border-top: 1px solid var(--color-tone-4);\n  }\n\n  .example {\n    margin-top: 24px;\n    margin-bottom: 24px;\n  }\n\n  game-tile {\n    width: 40px;\n    height: 40px;\n  }\n\n  :host([page]) section {\n    padding: 16px;\n    padding-top: 0px;\n  }\n\n  </style>\n  <section>\n    <div class="instructions">\n      <p>Guess the <strong>WORDLE</strong> in six tries.</p>\n      <p>Each guess must be a valid five-letter word. Hit the enter button to submit.</p>\n      <p>After each guess, the color of the tiles will change to show how close your guess was to the word.</p>\n      <div class="examples">\n        <p><strong>Examples</strong></p>\n        <div class="example">\n          <div class="row">\n            <game-tile letter="w" evaluation="correct" reveal></game-tile>\n            <game-tile letter="e"></game-tile>\n            <game-tile letter="a"></game-tile>\n            <game-tile letter="r"></game-tile>\n            <game-tile letter="y"></game-tile>\n          </div>\n          <p>The letter <strong>W</strong> is in the word and in the correct spot.</p>\n        </div>\n        <div class="example">\n          <div class="row">\n            <game-tile letter="p"></game-tile>\n            <game-tile letter="i" evaluation="present" reveal></game-tile>\n            <game-tile letter="l"></game-tile>\n            <game-tile letter="l"></game-tile>\n            <game-tile letter="s"></game-tile>\n          </div>\n          <p>The letter <strong>I</strong> is in the word but in the wrong spot.</p>\n        </div>\n        <div class="example">\n          <div class="row">\n            <game-tile letter="v"></game-tile>\n            <game-tile letter="a"></game-tile>\n            <game-tile letter="g"></game-tile>\n            <game-tile letter="u" evaluation="absent" reveal></game-tile>\n            <game-tile letter="e"></game-tile>\n          </div>\n          <p>The letter <strong>U</strong> is not in the word in any spot.</p>\n        </div>\n      </div>\n      <p><strong>A new WORDLE will be available each day!<strong></p>\n    </div>\n  </section>\n';
    var Qs = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), (e = a.call(this)).attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "connectedCallback",
            value: function() {
                this.shadowRoot.appendChild(Ks.content.cloneNode(!0))
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("game-help", Qs);
    var et = document.createElement("template");
    et.innerHTML = "\n  <style>\n    .overlay {\n      display: none;\n      position: absolute;\n      width: 100%;\n      height: 100%;\n      top: 0;\n      left: 0;\n      justify-content: center;\n      background-color: var(--color-background);\n      animation: SlideIn 100ms linear;\n      z-index: ".concat(2e3, ';\n    }\n\n    :host([open]) .overlay {\n      display: flex;\n    }\n\n    .content {\n      position: relative;\n      color: var(--color-tone-1);\n      padding: 0 32px;\n      max-width: var(--game-max-width);\n      width: 100%;\n      overflow-y: auto;\n      height: 100%;\n      display: flex;\n      flex-direction: column;\n    }\n\n    .content-container {\n      height: 100%;\n    }\n\n    .overlay.closing {\n      animation: SlideOut 150ms linear;\n    }\n\n    header {\n      display: flex;\n      justify-content: center;\n      align-items: center;\n      position: relative;\n    }\n\n    h1 {\n      font-weight: 700;\n      font-size: 16px;\n      letter-spacing: 0.5px;\n      text-transform: uppercase;\n      text-align: center;\n      margin-bottom: 10px;\n    }\n\n    game-icon {\n      position: absolute;\n      right: 0;\n      user-select: none;\n      cursor: pointer;\n    }\n\n    @media only screen and (min-device-width : 320px) and (max-device-width : 480px) {\n      .content {\n        max-width: 100%;\n        padding: 0;\n      }\n      game-icon {\n        padding: 0 16px;\n      }\n    }\n\n    @keyframes SlideIn {\n      0% {\n        transform: translateY(30px);\n        opacity: 0;\n      }\n      100% {\n        transform: translateY(0px);\n        opacity: 1;\n      }\n    }\n    @keyframes SlideOut {\n      0% {\n        transform: translateY(0px);\n        opacity: 1;\n      }\n      90% {\n        opacity: 0;\n      }\n      100% {\n        opacity: 0;\n        transform: translateY(60px);\n      }\n    }\n  </style>\n  <div class="overlay">\n    <div class="content">\n      <header>\n        <h1><slot></slot></h1>\n        <game-icon icon="close"></game-icon>\n      </header>\n      <div class="content-container">\n        <slot name="content"></slot>\n      </div>\n    </div>\n  </div>\n');
    var at = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), (e = a.call(this)).attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "connectedCallback",
            value: function() {
                var e = this;
                this.shadowRoot.appendChild(et.content.cloneNode(!0)), this.shadowRoot.querySelector("game-icon").addEventListener("click", (function(a) {
                    e.shadowRoot.querySelector(".overlay").classList.add("closing")
                })), this.shadowRoot.addEventListener("animationend", (function(a) {
                    "SlideOut" === a.animationName && (e.shadowRoot.querySelector(".overlay").classList.remove("closing"), Array.from(e.childNodes).forEach((function(a) {
                        e.removeChild(a)
                    })), e.removeAttribute("open"))
                }))
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("game-page", at);
    var st = document.createElement("template");
    st.innerHTML = '\n  <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24">\n    <path fill=var(--color-tone-1) />\n  </svg>\n';
    var tt = {
            help: "M11 18h2v-2h-2v2zm1-16C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14c-2.21 0-4 1.79-4 4h2c0-1.1.9-2 2-2s2 .9 2 2c0 2-3 1.75-3 5h2c0-2.25 3-2.5 3-5 0-2.21-1.79-4-4-4z",
            settings: "M19.14,12.94c0.04-0.3,0.06-0.61,0.06-0.94c0-0.32-0.02-0.64-0.07-0.94l2.03-1.58c0.18-0.14,0.23-0.41,0.12-0.61 l-1.92-3.32c-0.12-0.22-0.37-0.29-0.59-0.22l-2.39,0.96c-0.5-0.38-1.03-0.7-1.62-0.94L14.4,2.81c-0.04-0.24-0.24-0.41-0.48-0.41 h-3.84c-0.24,0-0.43,0.17-0.47,0.41L9.25,5.35C8.66,5.59,8.12,5.92,7.63,6.29L5.24,5.33c-0.22-0.08-0.47,0-0.59,0.22L2.74,8.87 C2.62,9.08,2.66,9.34,2.86,9.48l2.03,1.58C4.84,11.36,4.8,11.69,4.8,12s0.02,0.64,0.07,0.94l-2.03,1.58 c-0.18,0.14-0.23,0.41-0.12,0.61l1.92,3.32c0.12,0.22,0.37,0.29,0.59,0.22l2.39-0.96c0.5,0.38,1.03,0.7,1.62,0.94l0.36,2.54 c0.05,0.24,0.24,0.41,0.48,0.41h3.84c0.24,0,0.44-0.17,0.47-0.41l0.36-2.54c0.59-0.24,1.13-0.56,1.62-0.94l2.39,0.96 c0.22,0.08,0.47,0,0.59-0.22l1.92-3.32c0.12-0.22,0.07-0.47-0.12-0.61L19.14,12.94z M12,15.6c-1.98,0-3.6-1.62-3.6-3.6 s1.62-3.6,3.6-3.6s3.6,1.62,3.6,3.6S13.98,15.6,12,15.6z",
            backspace: "M22 3H7c-.69 0-1.23.35-1.59.88L0 12l5.41 8.11c.36.53.9.89 1.59.89h15c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H7.07L2.4 12l4.66-7H22v14zm-11.59-2L14 13.41 17.59 17 19 15.59 15.41 12 19 8.41 17.59 7 14 10.59 10.41 7 9 8.41 12.59 12 9 15.59z",
            close: "M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z",
            share: "M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92s2.92-1.31 2.92-2.92c0-1.61-1.31-2.92-2.92-2.92zM18 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM6 13c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm12 7.02c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z",
            statistics: "M16,11V3H8v6H2v12h20V11H16z M10,5h4v14h-4V5z M4,11h4v8H4V11z M20,19h-4v-6h4V19z"
        },
        nt = function(e) {
            r(t, e);
            var a = h(t);

            function t() {
                var e;
                return s(this, t), (e = a.call(this)).attachShadow({
                    mode: "open"
                }), e
            }
            return n(t, [{
                key: "connectedCallback",
                value: function() {
                    this.shadowRoot.appendChild(st.content.cloneNode(!0));
                    var e = this.getAttribute("icon");
                    this.shadowRoot.querySelector("path").setAttribute("d", tt[e]), "backspace" === e && this.shadowRoot.querySelector("path").setAttribute("fill", "var(--color-tone-1)"), "share" === e && this.shadowRoot.querySelector("path").setAttribute("fill", "var(--white)")
                }
            }]), t
        }(u(HTMLElement));
    customElements.define("game-icon", nt);
    var ot = document.createElement("template");
    ot.innerHTML = '\n  <a href="https://nytimes.com/puzzles">\n  <svg\n    className="pz-nav__logo"\n    width="95"\n    height="18"\n    viewBox="0 0 138 25"\n    fill="none"\n    xmlns="http://www.w3.org/2000/svg"\n    aria-label="New York Times Games Logo. Click for more puzzles"\n  >\n    <rect width="138" height="25" fill="none" />\n    <path\n      d="M42.4599 1.03519C44.219 1.00558 45.9577 1.41634 47.5176 2.23008V1.45245H53.4162V8.80515H47.5239C47.1067 7.03494 46.3607 6.2257 44.5904 6.2257C42.365 6.23834 41.0058 7.86947 41.0058 12.4151C41.0058 17.3148 42.2386 18.8827 45.0077 18.8827C45.7187 18.8975 46.4203 18.7183 47.0371 18.3643V16.2211H45.2037V11.9283H53.4225V24.0543H48.3648V22.9289C46.902 24.0012 45.1195 24.5471 43.307 24.4778C36.9216 24.4778 32.4392 20.2546 32.4392 12.4214C32.4708 5.2584 36.9849 1.03519 42.4599 1.03519Z"\n      fill=var(--color-tone-1)\n    />\n    <path\n      d="M59.8645 24.3471C56.3494 24.3471 54.2883 22.4505 54.2883 19.2198C54.2883 15.9892 56.7097 13.9345 60.541 13.9345C61.9923 13.9222 63.4232 14.2767 64.701 14.965C64.6377 13.2264 63.3164 12.0947 60.8634 12.0947C59.0925 12.1015 57.3477 12.5215 55.7677 13.3212V9.25608C58.149 8.58084 60.6136 8.24457 63.0888 8.25718C69.7966 8.25718 72.0853 11.1907 72.0853 13.7701V19.8647H73.4382V24.0563H64.7705V22.5074C63.544 23.8603 61.7359 24.3471 59.8645 24.3471ZM64.859 18.8658C64.888 18.6431 64.8655 18.4166 64.7931 18.204C64.7207 17.9914 64.6005 17.7982 64.4417 17.6394C64.2829 17.4805 64.0897 17.3603 63.877 17.288C63.6644 17.2156 63.438 17.193 63.2153 17.222C62.1215 17.222 61.3755 17.7721 61.3755 18.8974C61.3755 20.0228 62.0077 20.478 63.1836 20.478C64.3596 20.478 64.8653 19.9911 64.8653 18.8848L64.859 18.8658Z"\n      fill=var(--color-tone-1)\n    />\n    <path\n      d="M75.8371 19.8644V12.7709H74.5726V8.57927H83.1455V10.2546C85.1433 8.73732 86.2055 8.25684 87.786 8.25684C89.7206 8.25684 90.8839 8.80687 92.3949 10.3874C94.3611 8.83848 95.7456 8.25684 97.4526 8.25684C100.614 8.25684 102.801 10.419 102.801 13.2197V19.858H104.066V24.0496H95.5054V14.6739C95.5054 13.4473 95.0249 12.7772 94.1841 12.7772C93.3432 12.7772 92.9576 13.4094 92.9576 14.6739V19.8644H94.0513V24.056H85.6681V14.6106C85.6681 13.5169 85.1497 12.7709 84.4036 12.7709C83.6576 12.7709 83.1392 13.479 83.1392 14.6106V19.8644H84.2646V24.056H74.5474V19.8644H75.8371Z"\n      fill=var(--color-tone-1)\n    />\n    <path\n      d="M113.781 24.3784C111.46 24.3784 108.881 23.8979 107.073 22.2858C106.216 21.5344 105.534 20.6058 105.072 19.5643C104.61 18.5229 104.38 17.3935 104.398 16.2544C104.398 11.1967 108.432 8.25684 113.25 8.25684C118.453 8.25684 121.924 11.93 121.924 16.3555C121.924 16.874 121.892 17.3545 121.86 17.8729H111.745C111.941 19.681 112.908 20.4839 114.387 20.4839C114.871 20.4803 115.347 20.3544 115.769 20.1178C116.191 19.8813 116.547 19.5418 116.803 19.131H121.86C120.773 22.6777 117.498 24.3784 113.781 24.3784ZM111.688 15.5273H115.481V15.1417C115.481 13.8204 115.159 12.4674 113.585 12.4674C113.201 12.4558 112.824 12.5691 112.51 12.7903C112.197 13.0115 111.964 13.3286 111.846 13.6939C111.68 14.2856 111.624 14.9028 111.682 15.5147L111.688 15.5273Z"\n      fill=var(--color-tone-1)\n    />\n    <path\n      d="M126.195 24.059H122.712V18.8875H126.164C126.581 20.2404 127.131 20.9485 128.452 20.9485C129.451 20.9485 130.064 20.5313 130.064 19.7536C130.064 19.2036 129.71 18.7863 129.034 18.4892L125.683 17.073C124.909 16.7631 124.246 16.2281 123.779 15.5371C123.313 14.8462 123.064 14.0312 123.066 13.1975C123.066 10.5549 125.677 8.23462 128.964 8.23462C130.352 8.25084 131.718 8.58156 132.96 9.20191V8.5697H136.469V13.4062H133.244C132.954 11.9584 132.372 11.244 131.215 11.244C130.374 11.244 129.729 11.6612 129.729 12.3377C129.729 12.9194 130.115 13.3998 130.924 13.7223L134.212 14.9867C136.374 15.8276 137.373 17.2121 137.373 19.0835C137.373 22.0486 134.844 24.3372 131.215 24.3372C129.603 24.3372 128.477 24.078 126.157 23.2435L126.195 24.059Z"\n      fill=var(--color-tone-1)\n    />\n    <path\n      d="M25.9544 1.46704H25.3601V24.0372H25.9544V1.46704Z"\n      fill=var(--color-tone-1)\n    />\n    <path\n      d="M19.2574 15.4535C18.8889 16.497 18.3042 17.4509 17.5416 18.2527C16.7789 19.0546 15.8555 19.6863 14.8318 20.1066V15.4535L17.3607 13.1586L14.8318 10.8952V7.69619C15.8763 7.67489 16.8715 7.24792 17.6067 6.50567C18.3419 5.76342 18.7593 4.76418 18.7706 3.71953C18.7706 0.975708 16.1532 0.00209168 14.6675 0.00209168C14.2653 -0.0102783 13.8633 0.0322617 13.4726 0.128535V0.261301C13.6686 0.261301 13.9594 0.22969 14.0542 0.22969C15.0847 0.22969 15.8624 0.716498 15.8624 1.65218C15.8562 1.85411 15.809 2.05266 15.7235 2.23571C15.638 2.41875 15.5161 2.58244 15.3652 2.71677C15.2143 2.85109 15.0376 2.95323 14.8459 3.01695C14.6542 3.08066 14.4515 3.1046 14.2502 3.08732C11.7213 3.08732 8.693 1.01996 5.43075 1.01996C2.52255 1.00732 0.537385 3.17583 0.537385 5.36962C0.537385 7.56342 1.80182 8.24622 3.12316 8.7267L3.15477 8.60026C2.91743 8.45028 2.72511 8.23886 2.59822 7.98842C2.47133 7.73797 2.41459 7.45785 2.43404 7.17777C2.4493 6.92796 2.51386 6.68363 2.62398 6.45888C2.73411 6.23414 2.88763 6.03341 3.07569 5.86826C3.26375 5.70312 3.48264 5.57683 3.71973 5.49668C3.95683 5.41652 4.20745 5.38408 4.45714 5.40124C7.20096 5.40124 11.6265 7.69619 14.3766 7.69619H14.6359V10.9268L12.107 13.1586L14.6359 15.4535V20.1572C13.5788 20.533 12.4638 20.7192 11.342 20.7072C7.07452 20.7072 4.38759 18.1215 4.38759 13.8287C4.37897 12.8127 4.51955 11.8009 4.80486 10.8257L6.93543 9.88999V19.3733L11.2661 17.4766V7.75941L4.88072 10.6044C5.17861 9.73458 5.646 8.93247 6.25588 8.24446C6.86575 7.55645 7.606 6.99621 8.43379 6.59613L8.40218 6.5013C4.13471 7.43698 0 10.6739 0 15.5167C0 21.1055 4.71635 25 10.2103 25C16.0267 25 19.3206 21.1245 19.3522 15.4725L19.2574 15.4535Z"\n      fill=var(--color-tone-1)\n    />\n  </svg>\n  </a>\n';
    var rt = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), (e = a.call(this)).attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "connectedCallback",
            value: function() {
                this.shadowRoot.appendChild(ot.content.cloneNode(!0))
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("nyt-icon", rt);
    var it = document.createElement("template");
    it.innerHTML = '\n<svg width="21" height="17" viewBox="0 0 21 17" fill="none" xmlns="http://www.w3.org/2000/svg">\n    <rect x="0.172974" width="20" height="3" rx="1.5" fill=var(--color-tone-1) />\n    <rect x="0.172974" y="7" width="20" height="3" rx="1.5" fill=var(--color-tone-1) />\n    <rect x="0.172974" y="14" width="20" height="3" rx="1.5" fill=var(--color-tone-1) />\n</svg>\n';
    var lt = function(e) {
        r(t, e);
        var a = h(t);

        function t() {
            var e;
            return s(this, t), (e = a.call(this)).attachShadow({
                mode: "open"
            }), e
        }
        return n(t, [{
            key: "connectedCallback",
            value: function() {
                this.shadowRoot.appendChild(it.content.cloneNode(!0))
            }
        }]), t
    }(u(HTMLElement));
    customElements.define("nav-icon", lt);
    var dt = document.createElement("template");
    dt.innerHTML = '\n  <div id="timer"></div>\n';
    var ct = 6e4,
        ut = 36e5,
        mt = function(e) {
            r(t, e);
            var a = h(t);

            function t() {
                var e;
                s(this, t), o(m(e = a.call(this)), "targetEpochMS", void 0), o(m(e), "intervalId", void 0), o(m(e), "$timer", void 0), e.attachShadow({
                    mode: "open"
                });
                var n = new Date;
                return n.setDate(n.getDate() + 1), n.setHours(0, 0, 0, 0), e.targetEpochMS = n.getTime(), e
            }
            return n(t, [{
                key: "padDigit",
                value: function(e) {
                    return e.toString().padStart(2, "0")
                }
            }, {
                key: "updateTimer",
                value: function() {
                    var e, a = (new Date).getTime(),
                        s = Math.floor(this.targetEpochMS - a);
                    if (s <= 0) e = "00:00:00";
                    else {
                        var t = Math.floor(s % 864e5 / ut),
                            n = Math.floor(s % ut / ct),
                            o = Math.floor(s % ct / 1e3);
                        e = "".concat(this.padDigit(t), ":").concat(this.padDigit(n), ":").concat(this.padDigit(o))
                    }
                    this.$timer.textContent = "NEVER!!"
                }
            }, {
                key: "connectedCallback",
                value: function() {
                    var e = this;
                    this.shadowRoot.appendChild(dt.content.cloneNode(!0)), this.$timer = this.shadowRoot.querySelector("#timer"), this.intervalId = setInterval((function() {
                        e.updateTimer()
                    }), 200)
                }
            }, {
                key: "disconnectedCallback",
                value: function() {
                    clearInterval(this.intervalId)
                }
            }]), t
        }(u(HTMLElement));
    return customElements.define("countdown-timer", mt), e.CountdownTimer = mt, e.GameApp = ms, e.GameHelp = Qs, e.GameIcon = nt, e.GameKeyboard = ks, e.GameModal = hs, e.GameNav = Ys, e.GamePage = at, e.GameRow = x, e.GameSettings = Ta, e.GameStats = Vs, e.GameSwitch = Zs, e.GameThemeManager = C, e.GameTile = v, e.GameToast = Ia, e.NYTIcon = rt, e.NavIcon = lt, e.NavModal = Js, Object.defineProperty(e, "__esModule", {
        value: !0
    }), e
}({});