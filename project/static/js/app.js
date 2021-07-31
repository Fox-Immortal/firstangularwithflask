var myApp = angular.module('myApp', ['ngRoute','angularCSS']);

myApp.config(function ($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'static/partials/test.html',
      controller: 'testController',
      css: 'static/css/test.css'
    })
    .when('/main', {
      templateUrl: static/partials/main.html,
      controller: 'mainController',
      css: static/css/main.css
    })
    .when('/hello', {
      templateUrl: 'static/partials/hi.html'
    })
    .otherwise({
      redirectTo: '/'
    });
});