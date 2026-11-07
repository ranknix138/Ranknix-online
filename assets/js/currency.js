/**
 * Ranknix Online - Global Smart Multi-Currency Engine
 * Instant Auto-Detection by Timezone (0ms delay) + GeoIP Fallback
 * Supported Currencies: PKR, AED, SAR, GBP, USD, EUR, CAD, AUD, JPY, CNY, RUB, INR, TRY, QAR
 */

(function () {
  const CURRENCIES = {
    PKR: { code: "PKR", symbol: "₨ ", name: "Pakistan (PKR)", flag: "🇵🇰", rate: 280, round: 100 },
    AED: { code: "AED", symbol: "AED ", name: "UAE / Dubai (AED)", flag: "🇦🇪", rate: 3.67, round: 1 },
    SAR: { code: "SAR", symbol: "SAR ", name: "Saudi Arabia (SAR)", flag: "🇸🇦", rate: 3.75, round: 1 },
    GBP: { code: "GBP", symbol: "£", name: "United Kingdom (GBP)", flag: "🇬🇧", rate: 0.78, round: 1 },
    USD: { code: "USD", symbol: "$", name: "United States (USD)", flag: "🇺🇸", rate: 1.0, round: 1 },
    EUR: { code: "EUR", symbol: "€", name: "Europe (EUR)", flag: "🇪🇺", rate: 0.92, round: 1 },
    CAD: { code: "CAD", symbol: "CA$ ", name: "Canada (CAD)", flag: "🇨🇦", rate: 1.38, round: 1 },
    AUD: { code: "AUD", symbol: "A$ ", name: "Australia (AUD)", flag: "🇦🇺", rate: 1.52, round: 1 },
    JPY: { code: "JPY", symbol: "¥", name: "Japan (JPY)", flag: "🇯🇵", rate: 155, round: 10 },
    CNY: { code: "CNY", symbol: "¥", name: "China (CNY)", flag: "🇨🇳", rate: 7.25, round: 1 },
    RUB: { code: "RUB", symbol: "₽ ", name: "Russia (RUB)", flag: "🇷🇺", rate: 96, round: 10 },
    INR: { code: "INR", symbol: "₹ ", name: "India (INR)", flag: "🇮🇳", rate: 84, round: 10 },
    TRY: { code: "TRY", symbol: "₺ ", name: "Turkey (TRY)", flag: "🇹🇷", rate: 34, round: 1 },
    QAR: { code: "QAR", symbol: "QAR ", name: "Qatar (QAR)", flag: "🇶🇦", rate: 3.64, round: 1 }
  };

  const COUNTRY_CURRENCY_MAP = {
    PK: "PKR",
    AE: "AED",
    SA: "SAR",
    QA: "QAR",
    GB: "GBP",
    UK: "GBP",
    US: "USD",
    CA: "CAD",
    AU: "AUD",
    JP: "JPY",
    CN: "CNY",
    RU: "RUB",
    IN: "INR",
    TR: "TRY",
    DE: "EUR", FR: "EUR", IT: "EUR", ES: "EUR", NL: "EUR",
    BE: "EUR", AT: "EUR", IE: "EUR", PT: "EUR", GR: "EUR",
    FI: "EUR", SE: "EUR", NO: "EUR", DK: "EUR", PL: "EUR"
  };

  function detectByTimezone() {
    try {
      const tz = (Intl.DateTimeFormat().resolvedOptions().timeZone || "").toLowerCase();
      if (tz.includes("karachi") || tz.includes("pakistan")) return "PKR";
      if (tz.includes("dubai") || tz.includes("muscat") || tz.includes("abu_dhabi")) return "AED";
      if (tz.includes("riyadh") || tz.includes("saudi")) return "SAR";
      if (tz.includes("qatar") || tz.includes("doha")) return "QAR";
      if (tz.includes("london") || tz.includes("belfast")) return "GBP";
      if (tz.includes("tokyo")) return "JPY";
      if (tz.includes("shanghai") || tz.includes("chongqing") || tz.includes("urumqi") || tz.includes("hong_kong") || tz.includes("beijing") || tz.includes("taipei")) return "CNY";
      if (tz.includes("moscow") || tz.includes("samara") || tz.includes("yekaterinburg") || tz.includes("novosibirsk") || tz.includes("krasnoyarsk") || tz.includes("irkutsk") || tz.includes("yakutsk") || tz.includes("vladivostok")) return "RUB";
      if (tz.includes("kolkata") || tz.includes("calcutta") || tz.includes("india")) return "INR";
      if (tz.includes("istanbul")) return "TRY";
      if (tz.includes("toronto") || tz.includes("vancouver") || tz.includes("edmonton") || tz.includes("montreal") || tz.includes("winnipeg") || tz.includes("halifax")) return "CAD";
      if (tz.includes("sydney") || tz.includes("melbourne") || tz.includes("brisbane") || tz.includes("perth") || tz.includes("adelaide")) return "AUD";
      if (tz.includes("berlin") || tz.includes("paris") || tz.includes("rome") || tz.includes("madrid") || tz.includes("amsterdam") || tz.includes("brussels") || tz.includes("vienna") || tz.includes("dublin") || tz.includes("lisbon") || tz.includes("athens") || tz.includes("helsinki") || tz.includes("warsaw") || tz.includes("prague")) return "EUR";
      if (tz.includes("new_york") || tz.includes("chicago") || tz.includes("los_angeles") || tz.includes("denver") || tz.includes("phoenix") || tz.includes("america")) return "USD";
    } catch (e) {}
    return null;
  }

  function detectByIP(callback) {
    // 1st Priority: ipwho.is (fast & detailed)
    fetch("https://ipwho.is/")
      .then((res) => res.json())
      .then((data) => {
        if (data && data.success && data.country_code) {
          const code = data.country_code.toUpperCase();
          const curr = COUNTRY_CURRENCY_MAP[code] || (data.is_eu ? "EUR" : null);
          if (curr) callback(curr);
        }
      })
      .catch(() => {
        // Fallback: country.is
        fetch("https://api.country.is/")
          .then((res) => res.json())
          .then((data) => {
            if (data && data.country) {
              const code = data.country.toUpperCase();
              const curr = COUNTRY_CURRENCY_MAP[code] || null;
              if (curr) callback(curr);
            }
          })
          .catch(() => {});
      });
  }

  function formatPrice(baseUsd, currCode) {
    if (!baseUsd) return "";
    const str = String(baseUsd).trim();
    if (str.toLowerCase().includes("custom")) {
      return str;
    }
    const clean = str.replace(/[^0-9.]/g, "");
    const num = parseFloat(clean);
    if (isNaN(num)) return str;

    const cfg = CURRENCIES[currCode] || CURRENCIES.USD;
    let val = num * cfg.rate;
    if (cfg.round === 100) {
      val = Math.round(val / 100) * 100;
    } else if (cfg.round === 10) {
      val = Math.round(val / 10) * 10;
    } else {
      val = Math.round(val);
    }
    return `${cfg.symbol}${val.toLocaleString()}`;
  }

  function applyCurrency(currCode, isManual) {
    if (!CURRENCIES[currCode]) currCode = "USD";
    window.RanknixCurrency.current = currCode;

    if (isManual) {
      try {
        localStorage.setItem("ranknix_currency_manual", currCode);
        localStorage.setItem("ranknix_currency", currCode);
      } catch (e) {}
    } else {
      try {
        localStorage.setItem("ranknix_currency", currCode);
      } catch (e) {}
    }

    const cfg = CURRENCIES[currCode];

    // 1. Update dropdown active label
    document.querySelectorAll("#active-currency-label, .active-currency-label").forEach((el) => {
      el.textContent = `${cfg.flag} ${currCode}`;
    });

    // 2. Highlight buttons/pills in dropdowns and pricing bars
    document.querySelectorAll("[data-set-currency], [data-curr-pill], [data-sub-curr]").forEach((btn) => {
      const btnCurr =
        btn.getAttribute("data-set-currency") ||
        btn.getAttribute("data-curr-pill") ||
        btn.getAttribute("data-sub-curr");
      if (btnCurr === currCode) {
        btn.classList.add("bg-blue-50", "text-blue-600", "font-black");
        if (btn.classList.contains("curr-pill") || btn.classList.contains("sub-curr-pill")) {
          btn.classList.add("bg-blue-600", "text-white");
          btn.classList.remove("bg-blue-50", "text-blue-600", "text-slate-700");
        }
      } else {
        btn.classList.remove("bg-blue-50", "text-blue-600", "font-black", "bg-blue-600", "text-white");
        btn.classList.add("text-slate-700");
      }
    });

    // 3. Update all dynamic prices (.dynamic-price)
    document.querySelectorAll(".dynamic-price").forEach((el) => {
      const specificAttr = el.getAttribute("data-" + currCode.toLowerCase());
      if (specificAttr) {
        el.textContent = specificAttr;
      } else {
        const usdVal = el.getAttribute("data-usd") || el.getAttribute("data-pkr");
        if (usdVal) {
          let baseUsd = usdVal;
          if (!el.getAttribute("data-usd") && el.getAttribute("data-pkr")) {
            const pkrNum = parseFloat(String(usdVal).replace(/[^0-9.]/g, ""));
            if (!isNaN(pkrNum)) baseUsd = pkrNum / 280;
          }
          el.textContent = formatPrice(baseUsd, currCode);
        }
      }
    });

    // 4. Update PRICING_DATA plans if present
    if (window.PRICING_DATA) {
      for (const [planId, rates] of Object.entries(window.PRICING_DATA)) {
        const amountEl = document.getElementById(`price-${planId}`);
        if (amountEl) {
          if (rates[currCode]) {
            amountEl.textContent = rates[currCode].amount;
          } else if (rates.usdBase) {
            amountEl.textContent = formatPrice(rates.usdBase, currCode);
          } else if (rates.USD) {
            amountEl.textContent = formatPrice(rates.USD.amount, currCode);
          }
        }
      }
    }

    // 5. Update geo badges if present
    const geoBadge = document.getElementById("geo-currency-badge");
    if (geoBadge) {
      geoBadge.textContent = `${cfg.flag} Automatically displayed in ${cfg.name} based on your region`;
    }
  }

  // Public Interface
  window.RanknixCurrency = {
    currencies: CURRENCIES,
    current: "PKR",
    setCurrency: function (curr, isManual = true) {
      applyCurrency(curr, isManual);
    },
    format: function (usdVal, curr) {
      return formatPrice(usdVal, curr || window.RanknixCurrency.current);
    },
    init: function () {
      let initialCurr = null;

      // Check if user has explicitly picked a currency in the past
      try {
        const manual = localStorage.getItem("ranknix_currency_manual");
        if (manual && CURRENCIES[manual]) {
          initialCurr = manual;
        }
      } catch (e) {}

      // If no manual preference, auto-detect by Timezone immediately (0ms delay)
      if (!initialCurr) {
        const tzCurr = detectByTimezone();
        if (tzCurr && CURRENCIES[tzCurr]) {
          initialCurr = tzCurr;
        }
      }

      // Default fallback if unknown
      if (!initialCurr) {
        initialCurr = "PKR";
      }

      // Apply initial currency right away
      applyCurrency(initialCurr, false);

      // Async IP Geo verification (only overrides if user hasn't made a manual choice)
      try {
        if (!localStorage.getItem("ranknix_currency_manual")) {
          detectByIP((ipCurr) => {
            if (ipCurr && CURRENCIES[ipCurr] && ipCurr !== window.RanknixCurrency.current) {
              applyCurrency(ipCurr, false);
            }
          });
        }
      } catch (e) {}
    }
  };

  // Expose convenient global aliases
  window.setGlobalCurrency = function (curr, isManual) {
    window.RanknixCurrency.setCurrency(curr, isManual !== false);
  };
  window.changeGlobalCurrency = window.setGlobalCurrency;
  window.changePageCurrency = window.setGlobalCurrency;

  // Auto-init as soon as DOM is ready or immediately
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      window.RanknixCurrency.init();
    });
  } else {
    window.RanknixCurrency.init();
  }
})();
