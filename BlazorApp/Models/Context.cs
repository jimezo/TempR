using BlazorDB;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorApp
{
    public class Context
    {
        public StorageSet<Post> Posts { get; set; }
    }
}
