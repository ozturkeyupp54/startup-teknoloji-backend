/* @license lazysizes - v5.3.0 */
window.lazySizesConfig = {
        init: !1,
        expand: 10
    },
    function(e) {
        var t = function(n, f, s) {
            "use strict";
            var m, z;
            if (function() {
                    var e, t = {
                        lazyClass: "lazyload",
                        loadedClass: "lazyloaded",
                        loadingClass: "lazyloading",
                        preloadClass: "lazypreload",
                        errorClass: "lazyerror",
                        autosizesClass: "lazyautosizes",
                        fastLoadedClass: "ls-is-cached",
                        iframeLoadMode: 0,
                        srcAttr: "data-src",
                        srcsetAttr: "data-srcset",
                        sizesAttr: "data-sizes",
                        minSize: 40,
                        customMedia: {},
                        init: !0,
                        expFactor: 1.5,
                        hFac: .8,
                        loadMode: 2,
                        loadHidden: !0,
                        ricTimeout: 0,
                        throttleDelay: 125
                    };
                    for (e in z = n.lazySizesConfig || n.lazysizesConfig || {}, t) e in z || (z[e] = t[e])
                }(), !f || !f.getElementsByClassName) return {
                init: function() {},
                cfg: z,
                noSupport: !0
            };

            function o(e, t) {
                return de[t] || (de[t] = new RegExp("(\\s|^)" + t + "(\\s|$)")), de[t].test(e[ae]("class") || "") && de[t]
            }

            function c(e, t) {
                o(e, t) || e.setAttribute("class", (e[ae]("class") || "").trim() + " " + t)
            }

            function u(e, t) {
                (t = o(e, t)) && e.setAttribute("class", (e[ae]("class") || "").replace(t, " "))
            }

            function y(e, t, a, n, i) {
                var s = f.createEvent("Event");
                return (a = a || {}).instance = m, s.initEvent(t, !n, !i), s.detail = a, e.dispatchEvent(s), s
            }

            function h(e, t) {
                var a;
                !ee && (a = n.picturefill || z.pf) ? (t && t.src && !e[ae]("srcset") && e.setAttribute("srcset", t.src), a({
                    reevaluate: !0,
                    elements: [e]
                })) : t && t.src && (e.src = t.src)
            }

            function g(e, t) {
                return (getComputedStyle(e, null) || {})[t]
            }

            function i(e, t, a) {
                for (a = a || e.offsetWidth; a < z.minSize && t && !e._lazysizesWidth;) a = t.offsetWidth, t = t.parentNode;
                return a
            }

            function e(a, e) {
                return e ? function() {
                    fe(a)
                } : function() {
                    var e = this,
                        t = arguments;
                    fe(function() {
                        a.apply(e, t)
                    })
                }
            }

            function t(e) {
                function t() {
                    a = null, e()
                }
                var a, n, i = function() {
                    var e = s.now() - n;
                    e < 99 ? ie(i, 99 - e) : (oe || t)(t)
                };
                return function() {
                    n = s.now(), a = a || ie(i, 99)
                }
            }
            var a, r, l, p, v, C, b, d, A, E, _, w, M, N, L, x, S, W, B, T, F, R, D, k, H, O, P, $, q, I, U, j, G, J, K, Q, V, X, Y, Z = f.documentElement,
                ee = n.HTMLPictureElement,
                te = "addEventListener",
                ae = "getAttribute",
                ne = n[te].bind(n),
                ie = n.setTimeout,
                se = n.requestAnimationFrame || ie,
                oe = n.requestIdleCallback,
                re = /^picture$/i,
                le = ["load", "error", "lazyincluded", "_lazyloaded"],
                de = {},
                ce = Array.prototype.forEach,
                ue = function(t, a, e) {
                    var n = e ? te : "removeEventListener";
                    e && ue(t, a), le.forEach(function(e) {
                        t[n](e, a)
                    })
                },
                fe = (X = [], Y = V = [], we._lsFlush = _e, we),
                me = (R = /^img$/i, D = /^iframe$/i, k = "onscroll" in n && !/(gle|ing)bot/.test(navigator.userAgent), P = -1, x = ve, W = O = H = 0, B = z.throttleDelay, T = z.ricTimeout, F = oe && 49 < T ? function() {
                    oe(Ce, {
                        timeout: T
                    }), T !== z.ricTimeout && (T = z.ricTimeout)
                } : e(function() {
                    ie(Ce)
                }, !0), q = e(be), I = function(e) {
                    q({
                        target: e.target
                    })
                }, U = e(function(t, e, a, n, i) {
                    var s, o, r, l, d;
                    (r = y(t, "lazybeforeunveil", e)).defaultPrevented || (n && (a ? c(t, z.autosizesClass) : t.setAttribute("sizes", n)), s = t[ae](z.srcsetAttr), a = t[ae](z.srcAttr), i && (o = (d = t.parentNode) && re.test(d.nodeName || "")), l = e.firesLoad || "src" in t && (s || a || o), r = {
                        target: t
                    }, c(t, z.loadingClass), l && (clearTimeout(C), C = ie(ge, 2500), ue(t, I, !0)), o && ce.call(d.getElementsByTagName("source"), Ae), s ? t.setAttribute("srcset", s) : a && !o && (D.test(t.nodeName) ? (n = a, 0 == (d = (e = t).getAttribute("data-load-mode") || z.iframeLoadMode) ? e.contentWindow.location.replace(n) : 1 == d && (e.src = n)) : t.src = a), i && (s || o) && h(t, {
                        src: a
                    })), t._lazyRace && delete t._lazyRace, u(t, z.lazyClass), fe(function() {
                        var e = t.complete && 1 < t.naturalWidth;
                        l && !e || (e && c(t, z.fastLoadedClass), be(r), t._lazyCache = !0, ie(function() {
                            "_lazyCache" in t && delete t._lazyCache
                        }, 9)), "lazy" == t.loading && O--
                    }, !0)
                }), G = t(function() {
                    z.loadMode = 3, $()
                }), J = function() {
                    v || (s.now() - d < 999 ? ie(J, 999) : (v = !0, z.loadMode = 3, $(), ne("scroll", Ee, !0)))
                }, {
                    _: function() {
                        d = s.now(), m.elements = f.getElementsByClassName(z.lazyClass), p = f.getElementsByClassName(z.lazyClass + " " + z.preloadClass), ne("scroll", $, !0), ne("resize", $, !0), ne("pageshow", function(e) {
                            var t;
                            !e.persisted || (t = f.querySelectorAll("." + z.loadingClass)).length && t.forEach && se(function() {
                                t.forEach(function(e) {
                                    e.complete && j(e)
                                })
                            })
                        }), n.MutationObserver ? new MutationObserver($).observe(Z, {
                            childList: !0,
                            subtree: !0,
                            attributes: !0
                        }) : (Z[te]("DOMNodeInserted", $, !0), Z[te]("DOMAttrModified", $, !0), setInterval($, 999)), ne("hashchange", $, !0), ["focus", "mouseover", "click", "load", "transitionend", "animationend"].forEach(function(e) {
                            f[te](e, $, !0)
                        }), /d$|^c/.test(f.readyState) ? J() : (ne("load", J), f[te]("DOMContentLoaded", $), ie(J, 2e4)), m.elements.length ? (ve(), fe._lsFlush()) : $()
                    },
                    checkElems: $ = function(e) {
                        var t;
                        (e = !0 === e) && (T = 33), S || (S = !0, (t = B - (s.now() - W)) < 0 && (t = 0), e || t < 9 ? F() : ie(F, t))
                    },
                    unveil: j = function(e) {
                        var t, a, n, i;
                        e._lazyRace || (!(i = "auto" == (n = (a = R.test(e.nodeName)) && (e[ae](z.sizesAttr) || e[ae]("sizes")))) && v || !a || !e[ae]("src") && !e.srcset || e.complete || o(e, z.errorClass) || !o(e, z.lazyClass)) && (t = y(e, "lazyunveilread").detail, i && ze.updateElem(e, !0, e.offsetWidth), e._lazyRace = !0, O++, U(e, t, i, n, a))
                    },
                    _aLSL: Ee
                }),
                ze = (r = e(function(e, t, a, n) {
                    var i, s, o;
                    if (e._lazysizesWidth = n, n += "px", e.setAttribute("sizes", n), re.test(t.nodeName || ""))
                        for (s = 0, o = (i = t.getElementsByTagName("source")).length; s < o; s++) i[s].setAttribute("sizes", n);
                    a.detail.dataAttr || h(e, a.detail)
                }), {
                    _: function() {
                        a = f.getElementsByClassName(z.autosizesClass), ne("resize", l)
                    },
                    checkElems: l = t(function() {
                        var e, t = a.length;
                        if (t)
                            for (e = 0; e < t; e++) he(a[e])
                    }),
                    updateElem: he
                }),
                ye = function() {
                    !ye.i && f.getElementsByClassName && (ye.i = !0, ze._(), me._())
                };

            function he(e, t, a) {
                var n = e.parentNode;
                n && (a = i(e, n, a), (t = y(e, "lazybeforesizes", {
                    width: a,
                    dataAttr: !!t
                })).defaultPrevented || (a = t.detail.width) && a !== e._lazysizesWidth && r(e, n, t, a))
            }

            function ge(e) {
                O--, e && !(O < 0) && e.target || (O = 0)
            }

            function pe(e) {
                return (L = null == L ? "hidden" == g(f.body, "visibility") : L) || !("hidden" == g(e.parentNode, "visibility") && "hidden" == g(e, "visibility"))
            }

            function ve() {
                var e, t, a, n, i, s, o, r, l, d, c, u = m.elements;
                if ((b = z.loadMode) && O < 8 && (e = u.length)) {
                    for (t = 0, P++; t < e; t++)
                        if (u[t] && !u[t]._lazyRace)
                            if (!k || m.prematureUnveil && m.prematureUnveil(u[t])) j(u[t]);
                            else if ((o = u[t][ae]("data-expand")) && (i = +o) || (i = H), l || (l = !z.expand || z.expand < 1 ? 500 < Z.clientHeight && 500 < Z.clientWidth ? 500 : 370 : z.expand, d = (m._defEx = l) * z.expFactor, c = z.hFac, L = null, H < d && O < 1 && 2 < P && 2 < b && !f.hidden ? (H = d, P = 0) : H = 1 < b && 1 < P && O < 6 ? l : 0), r !== i && (A = innerWidth + i * c, E = innerHeight + i, s = -1 * i, r = i), d = u[t].getBoundingClientRect(), (N = d.bottom) >= s && (_ = d.top) <= E && (M = d.right) >= s * c && (w = d.left) <= A && (N || M || w || _) && (z.loadHidden || pe(u[t])) && (v && O < 3 && !o && (b < 3 || P < 4) || function(e, t) {
                            var a, n = e,
                                i = pe(e);
                            for (_ -= t, N += t, w -= t, M += t; i && (n = n.offsetParent) && n != f.body && n != Z;)(i = 0 < (g(n, "opacity") || 1)) && "visible" != g(n, "overflow") && (a = n.getBoundingClientRect(), i = M > a.left && w < a.right && N > a.top - 1 && _ < a.bottom + 1);
                            return i
                        }(u[t], i))) {
                        if (j(u[t]), n = !0, 9 < O) break
                    } else !n && v && !a && O < 4 && P < 4 && 2 < b && (p[0] || z.preloadAfterLoad) && (p[0] || !o && (N || M || w || _ || "auto" != u[t][ae](z.sizesAttr))) && (a = p[0] || u[t]);
                    a && !n && j(a)
                }
            }

            function Ce() {
                S = !1, W = s.now(), x()
            }

            function be(e) {
                var t = e.target;
                t._lazyCache ? delete t._lazyCache : (ge(e), c(t, z.loadedClass), u(t, z.loadingClass), ue(t, I), y(t, "lazyloaded"))
            }

            function Ae(e) {
                var t, a = e[ae](z.srcsetAttr);
                (t = z.customMedia[e[ae]("data-media") || e[ae]("media")]) && e.setAttribute("media", t), a && e.setAttribute("srcset", a)
            }

            function Ee() {
                3 == z.loadMode && (z.loadMode = 2), G()
            }

            function _e() {
                var e = Y;
                for (Y = V.length ? X : V, Q = !(K = !0); e.length;) e.shift()();
                K = !1
            }

            function we(e, t) {
                K && !t ? e.apply(this, arguments) : (Y.push(e), Q || (Q = !0, (f.hidden ? ie : se)(_e)))
            }
            return ie(function() {
                z.init && ye()
            }), m = {
                cfg: z,
                autoSizer: ze,
                loader: me,
                init: ye,
                uP: h,
                aC: c,
                rC: u,
                hC: o,
                fire: y,
                gW: i,
                rAF: fe
            }
        }(e, e.document, Date);
        e.lazySizes = t, "object" == typeof module && module.exports && (module.exports = t)
    }("undefined" != typeof window ? window : {});
/**
 * ThemeSphere lazyload extend.
 * @copyright ThemeSphere
 * @preserve
 */
! function() {
    let e = !1;

    function a(a, o) {
        var e = {};
        a.dataset.bgset && a.dataset.sizes ? (e.sizes = a.dataset.sizes, e.srcset = a.dataset.bgset) : e.src = a.dataset.bgsrc,
            function(e) {
                var t = e.dataset.ratio;
                if (0 < t) {
                    const a = e.parentElement;
                    if (a.classList.contains("media-ratio")) {
                        const o = a.style;
                        o.getPropertyValue("--a-ratio") || (o.paddingBottom = 100 / t + "%")
                    }
                }
            }(a);
        var t, n = document.createElement("img");
        for (t in n.onload = function() {
                var e = "url('" + (n.currentSrc || n.src) + "')",
                    t = a.style;
                t.backgroundImage !== e && requestAnimationFrame(() => {
                    t.backgroundImage = e, o && o()
                }), n.onload = null, n.onerror = null, n = null
            }, n.onerror = n.onload, e) n.setAttribute(t, e[t]);
        n && n.complete && 0 < n.naturalWidth && n.onload && n.onload()
    }

    function t(e) {
        var t = e => {
            a(e, () => {
                document.dispatchEvent(new Event("lazyloaded"))
            })
        };
        document.querySelectorAll(".img.bg-cover:not(.lazyload)").forEach(t), e && o(() => {
            document.querySelectorAll(".img.bg-cover").forEach(t)
        }), addEventListener("lazybeforeunveil", e => {
            var t = e.target;
            t.getAttribute("data-bgsrc") && (e.detail.firesLoad = !0, a(t, function() {
                window.lazySizes.fire(t, "_lazyloaded", {}, !0, !0)
            }))
        })
    }

    function o(e) {
        "complete" === document.readyState ? e() : window.addEventListener("load", e)
    }
    var n, r, d;
    e = BunyadLazy.type, e && window.lazySizes ? (t(), window.lazySizes.init(), "smart" !== e || document.documentElement.clientWidth < 1380 || (n = n || requestAnimationFrame, r = () => {
        document.querySelectorAll(".lazyload").forEach(e => {
            lazySizes.loader.unveil(e)
        })
    }, o(() => n(r, {
        timeout: 500
    }))), o(() => window.lazySizesConfig.expand = null), d = () => {
        document.querySelectorAll("script[data-type=lazy]").forEach(e => {
            e.src = e.dataset.src, e.dataset.type = ""
        })
    }, setTimeout(d, 4e3), o(() => {
        ["mousemove", "keydown", "touchstart"].forEach(e => document.addEventListener(e, d, {
            passive: !0,
            once: !0
        }))
    })) : t(!0)
}();