const INFO = {
  'Greenland': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Greenland', op: null, energy: 'https://ourworldindata.org/profile/energy/greenland' },
  'Canada': { pct: '0.2%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Canada', op: 'VIA Rail', energy: 'https://ourworldindata.org/profile/energy/canada' },
  'United States': { pct: '1%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_the_United_States', op: 'Amtrak', energy: 'https://ourworldindata.org/profile/energy/united-states' },
  'Mexico': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Mexico', op: null, energy: 'https://ourworldindata.org/profile/energy/mexico' },
  'Venezuela': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Venezuela', op: null, energy: 'https://ourworldindata.org/profile/energy/venezuela' },
  'Colombia': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Colombia', op: null, energy: 'https://ourworldindata.org/profile/energy/colombia' },
  'Brazil': { pct: '30%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Brazil', op: 'VALE / Rumo', energy: 'https://ourworldindata.org/profile/energy/brazil' },
  'Bolivia': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Bolivia', op: null, energy: 'https://ourworldindata.org/profile/energy/bolivia' },
  'Paraguay': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Paraguay', op: null, energy: 'https://ourworldindata.org/profile/energy/paraguay' },
  'Argentina': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Argentina', op: null, energy: 'https://ourworldindata.org/profile/energy/argentina' },
  'Algeria': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Algeria', op: null, energy: 'https://ourworldindata.org/profile/energy/algeria' },
  'Libya': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Libya', op: null, energy: 'https://ourworldindata.org/profile/energy/libya' },
  'Mauritania': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Mauritania', op: null, energy: 'https://ourworldindata.org/profile/energy/mauritania' },
  'Mali': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Mali', op: null, energy: 'https://ourworldindata.org/profile/energy/mali' },
  'Niger': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Niger', op: null, energy: 'https://ourworldindata.org/profile/energy/niger' },
  'Chad': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Chad', op: null, energy: 'https://ourworldindata.org/profile/energy/chad' },
  'Nigeria': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Nigeria', op: null, energy: 'https://ourworldindata.org/profile/energy/nigeria' },
  'Central African Republic': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_the_Central_African_Republic', op: null, energy: 'https://ourworldindata.org/profile/energy/central-african-republic' },
  'Democratic Republic of the Congo': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_the_Democratic_Republic_of_the_Congo', op: null, energy: 'https://ourworldindata.org/profile/energy/democratic-republic-of-congo' },
  'Angola': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Angola', op: null, energy: 'https://ourworldindata.org/profile/energy/angola' },
  'Namibia': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Namibia', op: null, energy: 'https://ourworldindata.org/profile/energy/namibia' },
  'Egypt': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Egypt', op: null, energy: 'https://ourworldindata.org/profile/energy/egypt' },
  'Sudan': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Sudan', op: null, energy: 'https://ourworldindata.org/profile/energy/sudan' },
  'Ethiopia': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Ethiopia', op: null, energy: 'https://ourworldindata.org/profile/energy/ethiopia' },
  'Kenya': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Kenya', op: null, energy: 'https://ourworldindata.org/profile/energy/kenya' },
  'Tanzania': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Tanzania', op: null, energy: 'https://ourworldindata.org/profile/energy/tanzania' },
  'Zambia': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Zambia', op: null, energy: 'https://ourworldindata.org/profile/energy/zambia' },
  'Zimbabwe': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Zimbabwe', op: null, energy: 'https://ourworldindata.org/profile/energy/zimbabwe' },
  'Mozambique': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Mozambique', op: null, energy: 'https://ourworldindata.org/profile/energy/mozambique' },
  'Madagascar': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Madagascar', op: null, energy: 'https://ourworldindata.org/profile/energy/madagascar' },
  'Turkey': { pct: '100%', wiki: 'https://en.wikipedia.org/wiki/State_Railways_of_the_Republic_of_Turkey', op: 'TCDD', energy: 'https://ourworldindata.org/profile/energy/turkey' },
  'Syria': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Syria', op: null, energy: 'https://ourworldindata.org/profile/energy/syria' },
  'Iraq': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Iraq', op: null, energy: 'https://ourworldindata.org/profile/energy/iraq' },
  'Saudi Arabia': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Saudi_Arabia', op: null, energy: 'https://ourworldindata.org/profile/energy/saudi-arabia' },
  'Yemen': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Yemen', op: null, energy: 'https://ourworldindata.org/profile/energy/yemen' },
  'Iran': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Iran', op: null, energy: 'https://ourworldindata.org/profile/energy/iran' },
  'Afghanistan': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Afghanistan', op: null, energy: 'https://ourworldindata.org/profile/energy/afghanistan' },
  'Pakistan': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Pakistan', op: null, energy: 'https://ourworldindata.org/profile/energy/pakistan' },
  'India': { pct: '99%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_India', op: 'Indian Railways', energy: 'https://ourworldindata.org/profile/energy/india' },
  'Kazakhstan': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Kazakhstan', op: null, energy: 'https://ourworldindata.org/profile/energy/kazakhstan' },
  'Mongolia': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Mongolia', op: null, energy: 'https://ourworldindata.org/profile/energy/mongolia' },
  'China': { pct: '75%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_China', op: 'China State Railway', energy: 'https://ourworldindata.org/profile/energy/china' },
  'Russia': { pct: '51%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Russia', op: 'Russian Railways', energy: 'https://ourworldindata.org/profile/energy/russia' },
  'Myanmar': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Myanmar', op: null, energy: 'https://ourworldindata.org/profile/energy/myanmar' },
  'Thailand': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Thailand', op: null, energy: 'https://ourworldindata.org/profile/energy/thailand' },
  'Cambodia': { pct: '0%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Cambodia', op: null, energy: 'https://ourworldindata.org/profile/energy/cambodia' },
  'Australia': { pct: '33%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Australia', op: null, energy: 'https://ourworldindata.org/profile/energy/australia' },
  'United Kingdom': { pct: '38%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Great_Britain', op: 'Network Rail', energy: 'https://ourworldindata.org/profile/energy/united-kingdom' },
  'France': { pct: '58%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_France', op: 'SNCF', energy: 'https://ourworldindata.org/profile/energy/france' },
  'Spain': { pct: '68%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Spain', op: 'Renfe', energy: 'https://ourworldindata.org/profile/energy/spain' },
  'Germany': { pct: '62%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Germany', op: 'Deutsche Bahn', energy: 'https://ourworldindata.org/profile/energy/germany' },
  'Poland': { pct: '64%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Poland', op: 'PKP', energy: 'https://ourworldindata.org/profile/energy/poland' },
  'Sweden': { pct: '75%', wiki: 'https://en.wikipedia.org/wiki/Rail_transport_in_Sweden', op: 'Trafikverket', energy: 'https://ourworldindata.org/profile/energy/sweden' }
};

const OPERATOR_URLS = {
  'Indian Railways': 'https://indianrailways.gov.in/',
  'Amtrak': 'https://www.amtrak.com/',
  'SNCF': 'https://www.sncf.com/',
  'Renfe': 'https://www.renfe.com/',
  'Deutsche Bahn': 'https://www.bahn.com/',
  'PKP': 'https://www.pkp.pl/',
  'TCDD': 'https://www.tcdd.gov.tr/',
  'Russian Railways': 'https://www.rzd.ru/',
  'China State Railway': 'http://www.china-railway.com.cn/',
  'VIA Rail': 'https://www.viarail.ca/',
  'Network Rail': 'https://www.networkrail.co.uk/',
  'Trafikverket': 'https://www.trafikverket.se/'
};

function initMapInteractivity() {
  document.querySelectorAll('.country-path').forEach(el => {
    el.addEventListener('click', function(e) {
      e.stopPropagation();
      const country = this.getAttribute('data-c');
      const d = INFO[country] || {
        pct: 'No figure on this map',
        wiki: 'https://en.wikipedia.org/wiki/Special:Search?search=' + encodeURIComponent('Rail transport in ' + country),
        op: null,
        energy: 'https://ourworldindata.org/profile/energy/' + encodeURIComponent(country.toLowerCase().replace(/\s+/g, '-'))
      };

      // Active highlight styling
      document.querySelectorAll('.country-path').forEach(p => p.classList.remove('active-country'));
      this.classList.add('active-country');

      const pctText = (d.pct === 'No figure on this map' || d.pct === null)
        ? 'No figure on this map'
        : (d.pct.includes('%') ? d.pct + ' of route electrified' : d.pct);

      const opLink = (d.op && OPERATOR_URLS[d.op])
        ? `<a class="panel-btn" target="_blank" rel="noopener" href="${OPERATOR_URLS[d.op]}"><b>2 &nbsp; National operator &mdash; ${d.op}</b><span>Official network operator site ↗</span></a>`
        : (d.op ? `<div class="panel-btn"><b>2 &nbsp; Operator &mdash; ${d.op}</b></div>` : '');

      const panelBody = document.getElementById('panel-body');
      panelBody.innerHTML = `
        <h2>${country}</h2>
        <p class="pct">${pctText}</p>
        <a class="panel-btn" target="_blank" rel="noopener" href="${d.wiki}"><b>1 &nbsp; Railway information</b><span>Network, operators, electrification and history ↗</span></a>
        ${opLink}
        <a class="panel-btn alt" target="_blank" rel="noopener" href="${d.energy}"><b>2 &nbsp; Electricity generation</b><span>Breakdown by primary energy source: coal, gas, oil, nuclear, hydro, wind, solar ↗</span></a>
      `;
      document.getElementById('info-panel').style.display = 'block';
    });
  });
}

// Load external map.svg into mapContainer
fetch('map.svg')
  .then(res => {
    if (!res.ok) throw new Error('Network response was not ok: ' + res.statusText);
    return res.text();
  })
  .then(svgText => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(svgText, 'image/svg+xml');
    const svgElement = doc.querySelector('svg');
    if (svgElement) {
      const loading = document.getElementById('map-loading');
      if (loading) loading.remove();
      document.getElementById('mapContainer').insertBefore(svgElement, document.getElementById('info-panel'));
      initMapInteractivity();
    }
  })
  .catch(err => {
    console.error('Failed to load map.svg:', err);
    const loading = document.getElementById('map-loading');
    if (loading) loading.textContent = 'Failed to load map.svg. Please run via a local server (e.g., http://127.0.0.1:8080).';
  });

function hidePanel() {
  document.getElementById('info-panel').style.display = 'none';
  document.querySelectorAll('.country-path').forEach(p => p.classList.remove('active-country'));
}

function toggleHighlights() {
  document.getElementById('mapContainer').classList.toggle('show-highlight-all');
}

// Modal Controls
function closeModal() {
  document.getElementById('modal-overlay').style.display = 'none';
  document.querySelectorAll('.modal-dialog').forEach(m => m.style.display = 'none');
  // Pause any playing videos when closing modal
  document.querySelectorAll('video').forEach(v => {
    v.pause();
  });
}

const modalOverlay = document.getElementById('modal-overlay');
if (modalOverlay) {
  modalOverlay.addEventListener('click', closeModal);
}

function openProfile(idx) {
  closeModal();
  document.getElementById('modal-overlay').style.display = 'block';
  document.getElementById('prof' + idx).style.display = 'block';
}

function openOppModal() {
  closeModal();
  document.getElementById('modal-overlay').style.display = 'block';
  document.getElementById('opp-modal').style.display = 'block';
}

function openVideoModal(idx) {
  closeModal();
  document.getElementById('modal-overlay').style.display = 'block';
  const targetModal = document.getElementById('video-modal-' + idx);
  if (targetModal) {
    targetModal.style.display = 'block';
    const videoElem = targetModal.querySelector('video');
    if (videoElem) {
      videoElem.currentTime = 0;
      videoElem.play().catch(e => console.log('Autoplay prevented:', e));
    }
  }
}
