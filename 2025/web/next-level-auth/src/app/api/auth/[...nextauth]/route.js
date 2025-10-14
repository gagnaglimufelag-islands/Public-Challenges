import NextAuth from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";

const users = [
  {
    id: "1",
    name: "Admin",
    username: process.env.ADMIN_USERNAME,
    password: process.env.ADMIN_PASS,
  },
];

export const authOptions = {
  session: {
    strategy: "jwt",
  },
  providers: [
    CredentialsProvider({
      name: "Credentials",
      credentials: {
        username: { label: "Username", type: "username", placeholder: "user" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        const user = users.find((u) => u.username === credentials.username);
        if (user && credentials.password == user.password) {
          return { id: user.id, name: user.name, username: user.username };
        }
        throw new Error("Invalid username or password");
      },
    }),
  ],
  secret: process.env.NEXTAUTH_SECRET,
};

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST };