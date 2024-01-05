using Microsoft.EntityFrameworkCore;

class PostcodeDb : DbContext
{
    public PostcodeDb(DbContextOptions<PostcodeDb> options)
        : base(options) { }

    public DbSet<Postcode> Postcodes => Set<Postcode>();
}
