(window.webpackJsonp=window.webpackJsonp||[]).push([[0],[,,,,,,,,function(e,t,o){e.exports=o.p+"static/media/logo.2b94c3e9.png"},function(e,t,o){e.exports=o(20)},,,,,,function(e,t,o){},function(e,t,o){},function(e,t,o){},function(e,t,o){},function(e,t,o){},function(e,t,o){"use strict";o.r(t);var n=o(0),l=o.n(n),r=o(7),a=o.n(r),i=(o(15),o(1)),d=o(2),c=o(4),s=o(3),m=o(5),u=(o(16),o(17),o(8)),f=o.n(u),v=function(e){function t(){return Object(i.a)(this,t),Object(c.a)(this,Object(s.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(d.a)(t,[{key:"render",value:function(){return n.createElement(n.Fragment,null,n.createElement("div",{className:"header"},n.createElement("img",{src:f.a,alt:"charity logo",className:"logo"}),n.createElement("h1",null,"Co-ordinator ",n.createElement("br",null),"dashboard"),n.createElement("div",{className:"commandBox"},n.createElement("i",{id:"welcomeInfo",className:"fas fa-info-circle"}),"Command box here")))}}]),t}(n.Component),C=(o(18),function(e){function t(){return Object(i.a)(this,t),Object(c.a)(this,Object(s.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(d.a)(t,[{key:"render",value:function(){return n.createElement(n.Fragment,null,n.createElement("div",{className:"job"},n.createElement("div",{className:"packageContents"},this.props.job.contents),n.createElement("div",{className:"transportFrom"},this.props.job.from),n.createElement("div",{className:"transportTo"},this.props.job.to),n.createElement("div",{className:"rider"},this.props.job.rider),n.createElement("div",{className:"timeOfCall"},this.props.job.timeOfCall),n.createElement("div",{className:"collected"},this.props.job.collected),n.createElement("div",{className:"delivered"},this.props.job.delivered)))}}]),t}(n.Component)),E=(o(19),function(e){function t(){return Object(i.a)(this,t),Object(c.a)(this,Object(s.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(d.a)(t,[{key:"render",value:function(){return n.createElement(n.Fragment,null,n.createElement("div",{className:"jobsList"},n.createElement("div",{className:"tableHeading"},n.createElement("div",null,n.createElement("div",null,"Contents"),n.createElement("div",null,"From"),n.createElement("div",null,"To"),n.createElement("div",null,"Rider"),n.createElement("div",null,"TOC"),n.createElement("div",null,"Collected at"),n.createElement("div",null,"Delivered at"))),this.props.filteredList.map(function(e,t){return n.createElement(C,{key:t,job:e})})))}}]),t}(n.Component)),b=[{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"North",collected:"1938",delivered:"2005"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"unassigned",collected:"1938",delivered:"en route"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"North",collected:"not yet",delivered:"not yet"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"North",collected:"1938",delivered:"2005"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"unassigned",collected:"1938",delivered:"en route"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"North",collected:"not yet",delivered:"not yet"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"unassigned",collected:"1938",delivered:"en route"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"North",collected:"not yet",delivered:"not yet"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"North",collected:"1938",delivered:"2005"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"unassigned",collected:"1938",delivered:"en route"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"},{timeOfCall:"1907",contents:"blood",from:"Eliz.Casson unit",to:"BRI A&E",rider:"North",collected:"not yet",delivered:"not yet"},{timeOfCall:"1907",contents:"milk",from:"SoutmeadNICU",to:"Weston Handover",rider:"West",collected:"1940",delivered:"en route"}],O=function(e){function t(){var e,o;Object(i.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(o=Object(c.a)(this,(e=Object(s.a)(t)).call.apply(e,[this].concat(l)))).state={filteredList:b},o}return Object(m.a)(t,e),Object(d.a)(t,[{key:"render",value:function(){return l.a.createElement(l.a.Fragment,null,l.a.createElement("div",{id:"myModal",className:"modal"},l.a.createElement("div",{className:"modal-content"},l.a.createElement("p",null,"This is the welcome modal"))),l.a.createElement(v,null),l.a.createElement(E,{filteredList:this.state.filteredList}))}}]),t}(n.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));a.a.render(l.a.createElement(O,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}],[[9,1,2]]]);
//# sourceMappingURL=main.adc42b2d.chunk.js.map