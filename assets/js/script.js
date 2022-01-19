document.addEventListener("DOMContentLoaded", function () {
  var sideNav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sideNav, {
      edge : "right"
  });

  var tabs = document.querySelectorAll(".tabs")
  M.Tabs.init(tabs, {})

  var collapsible = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsible, {});
});
