"use client";
import { useSession, signOut } from "next-auth/react";
import Link from "next/link";

export default function Home() {
  const { data: session } = useSession();

  return (
    <div style={{ textAlign: "center", padding: "2rem" }}>
      {session ? (
        <>
          <h2>Welcome, {session.user.name}!</h2>
          <Link href="/flag">
            <button>View flag</button>
          </Link>
          <button onClick={() => signOut()}>Sign out</button>
        </>
      ) : (
        <>
          <div className="hero-container">
            <h2>
              To view the flag, you must sign in using our <span className="highlight">patent-pending</span> multi-factor security
            </h2>
            <h3>
              Our security is so good that <strong>only prophets</strong> can see the flag.
              <br />
              Click the button below if you dare attempt this challenge.
            </h3>
            <Link href="/login">
              <button className="hero-button">Login</button>
            </Link>
          </div>
        </>
        
      )}
    </div>
  );
}