# ssh-keygen command

Generate, manage, and convert authentication keys for SSH.

## Overview

`ssh-keygen` creates public/private key pairs for SSH authentication, allowing secure passwordless logins to remote systems. It can also manage existing keys, convert between formats, and change key passphrases. The tool is essential for setting up secure remote access and automated connections between systems.

## Options

### **-t type**

Specifies the type of key to create (rsa, ed25519, ecdsa, dsa)

```console
$ ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_ed25519
Your public key has been saved in /home/user/.ssh/id_ed25519.pub
```

### **-f filename**

Specifies the filename of the key file

```console
$ ssh-keygen -t rsa -f ~/.ssh/github_key
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/github_key
Your public key has been saved in /home/user/.ssh/github_key.pub
```

### **-b bits**

Specifies the number of bits in the key (higher is more secure)

```console
$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_rsa
Your public key has been saved in /home/user/.ssh/id_rsa.pub
```

### **-p**

Changes the passphrase of an existing private key

```console
$ ssh-keygen -p -f ~/.ssh/id_rsa
Enter old passphrase: 
Enter new passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved with the new passphrase.
```

### **-c**

Changes the comment for a key

```console
$ ssh-keygen -c -f ~/.ssh/id_rsa -C "work laptop"
Enter passphrase: 
Key comment changed.
The comment in your key file has been changed.
```

## Usage Examples

### Creating a default SSH key

```console
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_rsa
Your public key has been saved in /home/user/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:abcdefghijklmnopqrstuvwxyz123456789ABCDEFG user@hostname
```

### Generating a key with custom settings

```console
$ ssh-keygen -t ed25519 -f ~/.ssh/server_key -C "server access key" -N "mypassphrase"
Generating public/private ed25519 key pair.
Your identification has been saved in /home/user/.ssh/server_key
Your public key has been saved in /home/user/.ssh/server_key.pub
The key fingerprint is:
SHA256:abcdefghijklmnopqrstuvwxyz123456789ABCDEFG server access key
```

### Viewing a key's fingerprint

```console
$ ssh-keygen -lf ~/.ssh/id_rsa.pub
3072 SHA256:abcdefghijklmnopqrstuvwxyz123456789ABCDEFG user@hostname (RSA)
```

## Tips

### Choose the Right Key Type
Ed25519 keys are recommended for most users as they provide strong security with smaller key sizes. RSA keys should be at least 3072 bits for good security.

### Protect Your Private Keys
Always keep your private keys secure and consider using a passphrase for important keys. The passphrase adds an extra layer of protection if someone gains access to your key file.

### Backup Your Keys
Store backups of your SSH keys in a secure location. Losing access to your private keys can mean losing access to systems that use them for authentication.

### Key Organization
Use meaningful filenames and comments for your keys to keep track of what each key is used for, especially if you maintain multiple keys for different services.

## Frequently Asked Questions

#### Q1. What is the difference between RSA and Ed25519 keys?
A. Ed25519 keys are newer, smaller, faster, and generally more secure than RSA keys. RSA keys are more widely supported but require larger key sizes (3072+ bits) for good security.

#### Q2. How do I add my SSH key to a remote server?
A. Copy your public key to the server using `ssh-copy-id username@server` or manually add the contents of your public key file to the server's `~/.ssh/authorized_keys` file.

#### Q3. Should I use a passphrase for my SSH key?
A. Yes, for better security. A passphrase protects your private key if someone gains access to your key file. For automation needs where typing a passphrase isn't practical, you can use ssh-agent to cache your passphrase.

#### Q4. How do I change or remove a key's passphrase?
A. Use `ssh-keygen -p -f ~/.ssh/your_key_file` to change the passphrase. Enter an empty passphrase to remove it entirely.

## macOS Considerations

On macOS, SSH keys are stored in the same location (`~/.ssh/`), but you may need to adjust permissions with `chmod 600 ~/.ssh/id_rsa` and `chmod 700 ~/.ssh` to ensure proper security. macOS also includes Keychain integration that can store your SSH key passphrases securely.

## References

https://man.openbsd.org/ssh-keygen.1

## Revisions

- 2025/04/30 First revision