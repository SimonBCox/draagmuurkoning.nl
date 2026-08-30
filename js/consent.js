// Toestemming en meting voor draagmuurkoning.nl
//
// Werking: Google Consent Mode v2 staat standaard op "geweigerd". Cookiebot
// toont de banner en zet de toestemming door naar Google. Pas na akkoord van
// de bezoeker laden Analytics en Ads daadwerkelijk.
//
// NOG INVULLEN voordat dit bestand wordt ingeladen:
//   GA4_ID  = meet-ID uit Analytics (Beheer > Gegevensstromen), begint met G-
//   ADS_ID  = conversie-ID uit Google Ads (Doelen > Conversies), begint met AW-
// Zolang beide leeg zijn, laadt er niets en gebeurt er niets.

var GA4_ID = "";
var ADS_ID = "";

// Consent Mode v2: alles dicht tot de bezoeker akkoord geeft.
window.dataLayer = window.dataLayer || [];
function gtag() { dataLayer.push(arguments); }
gtag("consent", "default", {
  ad_storage: "denied",
  ad_user_data: "denied",
  ad_personalization: "denied",
  analytics_storage: "denied",
  functionality_storage: "granted",
  security_storage: "granted",
  wait_for_update: 500
});
gtag("set", "ads_data_redaction", true);
gtag("set", "url_passthrough", true);

// De Google-tag zelf, één keer, zodra er een ID bekend is.
(function () {
  var id = GA4_ID || ADS_ID;
  if (!id) return;
  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + id;
  document.head.appendChild(s);
  gtag("js", new Date());
  if (GA4_ID) gtag("config", GA4_ID);
  if (ADS_ID) gtag("config", ADS_ID);
})();
