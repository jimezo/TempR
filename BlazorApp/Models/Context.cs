using BlazorDB;

namespace BlazorApp.Models
{
    public class Context : StorageContext
    {
        public StorageSet<Post> Posts { get; set; }
    }
}
