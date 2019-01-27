﻿using BlazorDB;
using Microsoft.AspNetCore.Blazor.Browser.Rendering;
using Microsoft.AspNetCore.Blazor.Browser.Services;
using Microsoft.AspNetCore.Blazor.Hosting;

namespace BlazorApp
{
    public class Program
    {
        public static void Main(string[] args)
        {

            var serviceProvider = new BrowserServiceProvider(services =>
            {
                services.AddBlazorDB(options =>
                {
                    options.LogDebug = true;
                    options.Assembly = typeof(Program).Assembly;
                });
            });
            new BrowserRenderer(serviceProvider).AddComponent<App>("app");

            CreateHostBuilder(args).Build().Run();
        }

        public static IWebAssemblyHostBuilder CreateHostBuilder(string[] args) =>
            BlazorWebAssemblyHost.CreateDefaultBuilder()
                .UseBlazorStartup<Startup>();
    }
}
